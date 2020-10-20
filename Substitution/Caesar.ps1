#!/snap/bin powershell

#Setting parameters
param(
    [Switch][Parameter(Mandatory=$false)]$encrypt,
    [Switch][Parameter(Mandatory=$false)]$decrypt,
    [string][Parameter(Mandatory=$true)]$text,
    [Parameter(Mandatory=$true)]$key
)

#Encoding Text
if ($encrypt) {
    [String]$final_result
    #$text="PowerShell Is So Cool"
    for ($i = 0; $i -lt $text.ToCharArray().Count; $i++){ #Splits String to Char
        if([Char]::IsWhiteSpace($text[$i])){ #Checking if there are any WhiteSpaces, and does nothing.
            $result = " "
        }
        Elseif([Char]::IsUpper($text[$i])){ #Encodes all UPPER letters in range 65 to 91
            $result = ([int]$text[$i] + $key - 65) % 26 + 65 
        }
        Elseif([Char]::IsLower($text[$i])){ #Encodes all Lower letters in range 97 to 123
            $result = ([int]$text[$i] + $key - 97) % 26 + 97
        }
        $final_result = -join($final_result, [char]$result) #Joins all chars and forms a string
    }
    Write-Host $final_result
}

#Decoding text
elseif ($decrypt) {
    #$text="UtbjwXmjqq Nx Xt Httq"
    [String]$final_result
    for ($i = 0; $i -lt $text.ToCharArray().Count; $i++) { #Splits String to Char
        if([Char]::IsWhiteSpace($text[$i])){ #Checking if there are any WhiteSpaces, and does nothing.
            $result = " "
        }
        Elseif([Char]::IsUpper($text[$i])){ #Decodes all UPPER letters in range 65 to 91
            $result = ([int]$text[$i] + (26-$key) - 65 ) % 26 + 65
        }
        Elseif([Char]::IsLower($text[$i])){ #Encodes all Lower letters in range 97 to 123
            $result = ([int]$text[$i] + (26-$key) - 97 ) % 26 + 97
        }
        $final_result = -join($final_result, [char]$result) #Joins all chars and forms a string
    }
    Write-Host $final_result
}

<#
$array= $text.ToCharArray() | ForEach-Object{[int][char]$_ -$key}  #Takes text and splits it into array, then converts to ANSCII numbers and subtracts $key
$Anscii_text = -join ($array | ForEach-Object{[char][int]$_}) #Joins each value in array together and converts it back to characters
Write-Output $array#>
