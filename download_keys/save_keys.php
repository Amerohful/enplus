<?
 header('Refresh: 0; url= ../index.php');  
ini_set ("session.use_trans_sid", true);
session_start();
 if (isset($_POST['ok'])){
  $keys = $_POST['key-words'];  
  $answer = $_POST['answer'];
  $count = count($keys);
  $fd = fopen("keys.txt", 'w') or die("не удалось создать файл");
  $str = "";
  for ($i=0; $i < $count-1; $i++) {
   $str = $str . $keys[$i] . "\n" . $answer[$i] . "\n";
 }
 $str = substr($str, 0, -1);
	$str = mb_convert_encoding($str, 'UTF-8', 'ANSI');
	fwrite($fd, $str);
   fclose($fd);
  
  


 }

?>