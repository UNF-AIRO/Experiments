<?php

class mainMenu {
        const INCLUDE_USER_INTERFACES = "
                                        <link rel='stylesheet' href='src/FOIL-UI-Framework-Library/FOIL-UI.css'>
                                        ";



        const SUB_HEADER_CONTENTS = "
                                        <div class='FOIL-Font-Styles--sans-serif'>
                                        <div class='FOIL-Navigation-Bar'>
                                       	<h1> Menu </h1>
                                        </div>
                                        <a href='shutdown.php' class='FOIL-Button color-is-red'>SHUTDOWN </a>
                                        <a href='restart.php' class='FOIL-Button color-is-red'>RESTART</a>
                                        </div>
                                    ";


        
}

echo mainMenu::INCLUDE_USER_INTERFACES;                 // ENABLE FOIL-UI
echo mainMenu::SUB_HEADER_CONTENTS;                     // ENABLE SUB HEADER CONTENTS

?>
