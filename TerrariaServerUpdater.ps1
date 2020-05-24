$terraria_install_path = "c:\Terraria\"
$terraria_zip_path = "$($terraria_install_path)Terraria.zip"

Import-Module BitsTransfer

Stop-Process -Name TerrariaServer

$web=wget -Uri https://terraria.org/ -UseBasicParsing
$href=$web.links|?{$_.outerHTML -like "*PC Dedicated Server*"}|select -Expand href
$dl_url="https://terraria.org/$href"

Start-BitsTransfer -Source $dl_url -Destination $terraria_zip_path
Expand-Archive -Path $terraria_zip_path -DestinationPath $terraria_install_path -Force

$fldr=Get-ChildItem -Path $terraria_install_path| ?{ $_.PSIsContainer }|Sort-Object -Property {$_.LastWriteTime} -Descending

Start-Process -WorkingDirectory $terraria_install_path -FilePath "$($terraria_install_path)$($fldr)\Windows\TerrariaServer.exe" -LoadUserProfile -WindowStyle Normal -ArgumentList "-config $($terraria_install_path)serverconfig-master.txt"
Start-Process -WorkingDirectory $terraria_install_path -FilePath "$($terraria_install_path)$($fldr)\Windows\TerrariaServer.exe" -LoadUserProfile -WindowStyle Normal -ArgumentList "-config $($terraria_install_path)serverconfig-journey.txt"

