rm -f posts.db
sqlite3 posts.db <<EOF
CREATE TABLE POSTS (AUTHOR TEXT NOT NULL, TITLE TEXT NOT NULL, CONTENT TEXT NOT NULL, EDITPWD TEXT NOT NULL, LASTEDIT TEXT NOT NULL);
INSERT INTO POSTS VALUES ("Aaron", "Hello, World!", "This is my first blog, accessible for everyone. <br>Maybe there's even a flag", "poke{h0w_d1d_y0u_g3t_my_secr3t_pwd}", "15.02.2021 14:00");
INSERT INTO POSTS VALUES ("Aaron", "Test Post", "I love SQLite, you can just scream all the time:<br>SELECT * FROM POSTS WHERE EDITPWD = 'test';", "Not_This_One_Either", "15.02.2021 14:11");
INSERT INTO POSTS VALUES ("Aaron", "You can do it too", "I thought I'd let you know you can edit your posts by clicking edit and using the password you specified during posting you can edit the post.", "Not_This_One", "15.02.2021 14:15");
INSERT INTO POSTS(AUTHOR, TITLE, CONTENT, LASTEDIT, EDITPWD) VALUES ('Aaron', '<b>Deleting posts</b>', 'You can now edit posts. <br>Also: The flag is the editpwd of the very first post.', 'Posted by the real Aaron, which can modify the time', 'ashdashdhxcnwernzewbzbuzsdasdasd');
EOF
chmod a+wx posts.db
