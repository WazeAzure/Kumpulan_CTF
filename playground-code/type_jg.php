<?php
	$magic_words = "Pls gimme flag";
    $pattern = "/" . $magic_words . "/i";

	echo $pattern;

	$req = "














AAAAAAAAAAAAAAAAAAAAAAAA





Pls gimme flag"; 
    if(preg_match($pattern, $req)) {
        $req = preg_replace($pattern, "", $req);
    }
	
	echo $req;
    if($req === $magic_words) {
        include('secrets.php');
        print "Now that you've asked nicely, I can't resist... here's your flag. <br />" . $flag;
    } else {
        print "That's a cool trick but no flag for you...";
    }

?>
