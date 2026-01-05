from amaranth import *
from amaranth.lib import wiring
from amaranth.lib.wiring import In, Out
from amaranth.lib.memory import Memory


class UpCounter(wiring.Component):
    """

    Parameters
    ----------

    Attributes
    ----------
    en : Signal, in
        The counter is incremented if ``en`` is asserted, and retains
        its value otherwise.
    ovf : Signal, out
        ``ovf`` is asserted when the counter reaches its limit.
    """

    en: In(1)
    done: Out(1)

    def __init__(self, grid):
        self.count = Signal(16)
        self.grid = grid

        super().__init__()

    def elaborate(self, platform):
        m = Module()

        msg = []

        width = len(grid[0])
        height = len(grid)

        STATE_SPLIT = 0b01
        STATE_EMPTY = 0b00
        STATE_STREIGHT = 0b10

        for yy in range(height):
            for xx in range(width):
                c = self.grid[yy][xx]
                if c == '^':
                    msg += [STATE_SPLIT]
                elif c == '.':
                    msg += [STATE_EMPTY]
                elif c == 'S':
                    msg += [STATE_STREIGHT]

        m.submodules.memory = memory = Memory(shape=unsigned(2), depth=len(msg), init=msg)

        rd_port = memory.read_port(domain="comb")
        rd_port_next_row = memory.read_port(domain="comb")
        wr_port = memory.write_port()
        #TODO: does this work on glasgow HW
        wr_port2 = memory.write_port()

        with m.If(self.en):
            with m.If(rd_port.addr == memory.depth - 1):
                m.d.sync += self.done.eq(1)
            with m.Else():
                m.d.sync += self.done.eq(0)

                # Move to next address
                m.d.sync += rd_port.addr.eq(rd_port.addr + 1)
                m.d.sync += rd_port_next_row.addr.eq(rd_port.addr + 1 + width)

                # If current cell is '|' and one under it is '.'
                # - Write '|' to lower one
                with m.If((rd_port.data == STATE_STREIGHT) & (rd_port_next_row.data == STATE_EMPTY)):
                    m.d.comb += wr_port.addr.eq(rd_port_next_row.addr)
                    m.d.comb += wr_port.en.eq(1)
                    m.d.comb += wr_port.data.eq(STATE_STREIGHT)
                    # Count is unchanged
                    m.d.sync += self.count.eq(self.count)
                with m.Else():
                    with m.If((rd_port.data == STATE_STREIGHT) & (rd_port_next_row.data == STATE_SPLIT)):
                        m.d.comb += wr_port.addr.eq(rd_port_next_row.addr - 1)
                        m.d.comb += wr_port.en.eq(1)
                        m.d.comb += wr_port.data.eq(STATE_STREIGHT)

                        m.d.comb += wr_port2.addr.eq(rd_port_next_row.addr + 1)
                        m.d.comb += wr_port2.en.eq(1)
                        m.d.comb += wr_port2.data.eq(STATE_STREIGHT)

                        # Count of splits increases
                        m.d.sync += self.count.eq(self.count + 1)
                    with m.Else():
                        # Count is unchanged
                        m.d.sync += self.count.eq(self.count)
        with m.Else():
            m.d.sync += self.done.eq(1)

        return m
# --- TEST ---
from amaranth.sim import Simulator

with open("input_full") as f:
    grid = [[x for x in y.strip()] for y in f.readlines()]

dut = UpCounter(grid)
async def bench(ctx):
    # Disabled -> do nothing
    ctx.set(dut.en, 0)
    await ctx.tick()
    assert ctx.get(dut.done)

    # Once enabled, the counter should overflow in 25 cycles.
    ctx.set(dut.en, 1)
    ctx.set(dut.done, 0)
    while not ctx.get(dut.done):
        await ctx.tick()
    print("Answer is: ", ctx.get(dut.count))
    await ctx.tick()



sim = Simulator(dut)
sim.add_clock(1e-6)
sim.add_testbench(bench)
with sim.write_vcd("up_counter.vcd"):
    sim.run()
# --- CONVERT ---
from amaranth.back import verilog


top = UpCounter(grid)
with open("up_counter.v", "w") as f:
    f.write(verilog.convert(top))


#TODO: comment, nix env, surfer, readme, cleanup, part2?
