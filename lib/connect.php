<?
@mysql_connect("localhost", "root")
  or die('connection error ' . mysql_error());
@mysql_select_db("bot");
?>