#!/snap/bin powershell

#Setting Parameters 
param(
    [Switch][Parameter(Mandatory=$false)]$encrypt,
    [Switch][Parameter(Mandatory=$false)]$decrypt,
    [string][Parameter(Mandatory=$true)]$text,
    [Parameter(Mandatory=$true)]$key
)

#Encryption
if ($encrypt){

    [String]$encrypt_text
    #$text="POWERSHELL"
    #$key=3
    
    $rows = [int][Math]::Ceiling($text.length/$key) #Number of rows
    $total_char = $key * $rows #Total characters
    $spaces = $total_char - $text.length

    $Empty_spot = ($key - $spaces) + 1 
    $a = ($rows * $Empty_spot) - 1 #startIndex

    foreach($i in 0..$key) { #Encodes the text
        foreach($j in 0..$text.length) {
            if($j % $key -eq $i) {
                $encrypt_text += $text[$j]
            }
            
        }
    }
    for($j = $a; $j -le $total_char; $j += $rows) { #Inserts "." for extra indexes
        $encrypt_text = $encrypt_text.insert($j, ".")
    }
    Write-Host $encrypt_text

#Decryption    
}elseif ($decrypt){

    [String]$decrypt_text
    #$text="PEOLWLE.R.S.H."
    #$key=7
    $rows = $text.length/$key

    for($i = 0; $i -lt $rows; $i++) {
        for($j = 0; $j -lt $key; $j++) {
            if(($i * $key) + $j -lt ($text.length)) { #Decrypting
                $decrypt_text += $text[$j * $rows + $i]
            }
        }
    }
    
    Write-Host $decrypt_text
}