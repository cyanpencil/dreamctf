<html>
	<head>
		<link rel="stylesheet" href="https://unpkg.com/purecss@2.0.5/build/pure-min.css" integrity="sha384-LTIDeidl25h2dPxrB2Ekgc9c7sEC3CWGM6HeFmuDNUjX76Ert4Z4IY714dhZHPLd" crossorigin="anonymous">
		<link rel="stylesheet" href="https://netdna.bootstrapcdn.com/font-awesome/4.0.3/css/font-awesome.css">
		<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/denali-css/css/denali.css">
		<link rel="stylesheet" href="/styles.css">
	</head>

		<body>
		<div class="header">
			<div class="home-menu pure-menu pure-menu-horizontal pure-menu-fixed">
				<a class="pure-menu-heading" href="">Blog 2.0</a>

				<ul class="pure-menu-list">
					<li class="pure-menu-item pure-menu-selected"><a href="#" class="pure-menu-link">Blog</a></li>
					<li class="pure-menu-item pure-menu-selected"><a href="#post" class="pure-menu-link">Post</a></li>
				</ul>
			</div>
		</div>

		<div class="splash-container">
			<div class="splash">
				<h1 class="splash-head">My new open blog</h1>
					<p class="splash-subhead">Welcome</p>
				</div>
			</div>
			<div class="footer l-box is-center">
			   Made from ETH DINFK Students, for ETH DINFK Students 
			</div>
		</div>	
		<div id="layout" class="content-wrapper">
			<div class="content">

<?php
$db = new SQLite3("posts.db");
function createPost($data, $pinned) {
	echo '<div class="posts is-center">';
	if ($pinned) { echo '<h1 class="content-subhead">Pinned Post</h1>'; }
	echo '<section class="post"><header class="post-header"><h2 class="post-title">';
	echo $data["TITLE"];
	echo '</h2><p class="post-meta">By <a class="post-author">';
	echo $data["AUTHOR"];
	echo '</a>, Last Edit ';
	echo $data["LASTEDIT"];
	echo ', <a href="#edit-post-';
	echo $data["rowid"];
	echo '">Edit</a></p></header><div class="post-description"><p>';
	echo $data["CONTENT"];
	echo '</p></div></section></div>';
	echo '<div id="edit-post-';
	echo $data["rowid"];
	echo '" class="modal"><div class="modal-container"><a href="#" class="close">X</a>';
	echo '<div class="modal-content"><form action="/edit.php", method="post">
		<textarea name="content" rows="50" required>';
	echo $data["CONTENT"];
	echo '</textarea>
		<input type="hidden" name="id" value="';
	echo $data["rowid"];
	echo '"/><input type="password" id="pass" name="pass" required>
		<input type="checkbox" name="delete"><label>Delete</label><br>
		<input type="submit" value="Edit">
		</form></div></div></div>';
}

$res = $db->query('SELECT rowid,* FROM POSTS WHERE rowid = 1')->fetchArray();
createPost($res, true);

$res = $db->query('SELECT rowid,* FROM POSTS ORDER BY rowid DESC');
while($row = $res->fetchArray()) {
	createPost($row, false);
}
?>

			</div>
		</div>
		<div id="success" class="modal">
			<div class="modal-container">
				<a href="#" class="close">X</a>'
				<div class="modal-content">
					<h1>Success</h1>
					<p>Successfully updated the post!</p>
				</div>
			</div>
		</div>
		<div id="successp" class="modal">
			<div class="modal-container">
				<a href="#" class="close">X</a>'
				<div class="modal-content">
					<h1>Success</h1>
					<p>Successfully posted with password <?php echo $_GET["pw"];  ?>!</p>
				</div>
			</div>
		</div>
		<div id="fail" class="modal">
			<div class="modal-container">
				<a href="#" class="close">X</a>'
				<div class="modal-content">
					<h1>Failure</h1>
					<p>Could not update the post! Perhaps you entered the wrong password.</p>
				</div>
			</div>
		</div>
		<div id="post" class="modal">
			<div class="modal-container">
				<a href="#" class="close">X</a>'
				<div class="modal-content">
					<h1>Create your post</h1>
					<form action="post.php" method="post">
						<label for="title">Title: </label><br>
						<input type="text" name="title" required><br>
						<label for="author">Author: </label><br>
						<input type="text" name="author" required><br>
						<label for="content">Content: </label><br>
						<textarea name="content" rows="25" required></textarea><br>
						<label for="pass">Password (For edits)</label><br>
						<input type="password" name="pass" required><br><br>
						<input type="submit" value="Post">
					</form> 
				</div>
			</div>
		</div>
	</body>
</html>
