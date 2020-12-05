$input = "yzbqklnj"
$md5 = new-object -TypeName System.Security.Cryptography.MD5CryptoServiceProvider
$utf8 = new-object -TypeName System.Text.UTF8Encoding

$value = 0;

while($TRUE)
{
    $inputValue = $input + $value
    $hash = [System.BitConverter]::ToString($md5.ComputeHash($utf8.GetBytes($inputValue)))
    $hashNoHyphen = $hash -replace "-", ""
    echo $hashNoHyphen

    #if part one change the number in the braces to 5, if part 2 change it to 6
    if($hashNoHyphen -match "^0{6}")
    {
        break;
    }

    $value = $value + 1
}

echo "Found hash:"
echo $inputValue
echo $hashNoHyphen
echo $value