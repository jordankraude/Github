Setting: <phpserver class="phpPath"></phpserver>
<Default:null></Default:null>
<?php

if($_POST["message"]) {

    mail("jordankraudeTP@gmail.com", "Here is the subject line",
    
    $_POST["insert your message here"]. "From: an@email.address");    
    
    }
    
    
?>

/* File->Preferences->settings->User settings tab->extensions->from the drop down select php->on the right pane under PHP › Validate: Executable Path select edit in settings.json.

Then set the path as your case may be e.g for a xamp user who installed xammp on c drive you will have:
*/
"php.validate.executablePath": "c:\\xampp\\php\\php.exe"

/*  If php is installed in your system independently or by other means simply set the path of your php.exe file like below:
*/
"php.validate.executablePath": "C://path.to.your.php.folder//php.exe"