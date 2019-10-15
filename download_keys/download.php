<?
ini_set ("session.use_trans_sid", true);
session_start();
  if (isset($_POST['ok'])){
   $keys = $_POST['keys']; 
   $answer = $_POST['answer'];
   $fd = fopen("keys.txt", 'a') or die("не удалось создать файл");
    fwrite($fd, $keys."\n".$answer."\n"."\n");
    fclose($fd);
    header('Location: http://bot.ru');    
  } //если была нажата кнопка 
?>