<?php

if (!isset($_POST['id'])) { die("No ID Specified"); }
if (!isset($_POST['content'])) { die("No new content Specified"); }
if (!isset($_POST['pass'])) { die("No Password Specified"); }

$id = $_POST['id'];
$content = $_POST['content'];
$pass = $_POST['pass'];
$del = $_POST['delete'] == 'on';

if(strpos($content, "<") !== false) {
	header('Location: /index.php#fail');
} else {
	$db = new SQLite3("posts.db");

	if($del) {
		$res = $db->prepare('DELETE FROM POSTS WHERE rowid = :id and EDITPWD = :pass');
		$res->bindValue(':id', $id);
		$res->bindValue(':pass', $pass);
		$a = $res->execute();
		header('Location: /index.php#success');
	} else {
		$res = $db->prepare('UPDATE POSTS SET CONTENT = :content, LASTEDIT = :time WHERE rowid = :id and EDITPWD = :pass');
		$res->bindValue(':content', $content);
		$res->bindValue(':id', $id);
		$res->bindValue(':pass', $pass);
		$res->bindValue(':time', date("d.m.Y H:i"));
		$a = $res->execute();
	
		$res = $db->prepare('SELECT CONTENT FROM POSTS WHERE rowid = :id and EDITPWD = :pass');
		$res->bindValue(':id', $id);
		$res->bindValue(':pass', $pass);
		$a = $res->execute();
	
		if($a->fetchArray() !== false) {
			header('Location: /index.php#success');
		} else {
			header('Location: /index.php#fail');
		}
	}
}

?>
