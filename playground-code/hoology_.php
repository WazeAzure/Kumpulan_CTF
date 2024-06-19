<?php

$url = "https://pastebin.com/raw/igdP9VGM";

echo htmlspecialchars(shell_exec('curl '. escapeshellcmd($url)));
?>
