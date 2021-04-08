<?php

if (!isset($_POST['author'])) { die("No Author Specified"); }
if (!isset($_POST['title'])) { die("No Title Specified"); }
if (!isset($_POST['content'])) { die("No Content Specified"); }
if (!isset($_POST['pass'])) { die("No Password for edits Specified"); }

$author = $_POST['author'];
$title = $_POST['title'];
$content = $_POST['content'];
$pass = $_POST['pass'];

if(strpos(strtolower($content), "recurse") !== false || strpos(strtolower($author), "recurse") !== false || strpos(strtolower($title), "recurse") !== false || strpos(strtolower($pass), "recurse") !== false) die("What the fuck man?");
if(strpos(strtolower($content), "flag") !== false || strpos(strtolower($author), "flag") !== false || strpos(strtolower($title), "flag") !== false || strpos(strtolower($pass), "flag") !== false) die("No flags here");
	
if(strpos($content, "<") !== false || strpos($author, "<") !== false || strpos($title, "<") !== false) { 
        header('Location: /index.php#fail');
} else {
	$db = new SQLite3("posts.db");
	$res = $db->prepare('INSERT INTO POSTS (AUTHOR, TITLE, CONTENT, LASTEDIT, EDITPWD) VALUES (:author, :title, :content, :time, \'' . $pass . '\')');

	if($res === false) die("Something went wrong...");
	
	$res->bindValue(':content', $content);
	$res->bindValue(':author', $author);
	$res->bindValue(':title', $title);
	$res->bindValue(':time', date("d.m.Y H:i"));

	$res->execute();

	$res = $db->prepare('SELECT EDITPWD FROM POSTS WHERE CONTENT = :content AND AUTHOR = :author AND TITLE = :title ORDER BY rowid DESC');
        $res->bindValue(':title', $title);
        $res->bindValue(':author', $author);
        $res->bindValue(':content', $content);
        $a = $res->execute()->fetchArray();

	if($a !== false) {
                header('Location: /index.php?pw=' . $a["EDITPWD"] . "#successp");
        } else {
                header('Location: /index.php#fail');       
        }

}

?>
