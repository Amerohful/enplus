<?

ini_set ("session.use_trans_sid", true);

session_start();

 if (isset($_POST['ok'])){

  $keys = $_POST['key-words'];  

  $answer = $_POST['answer'];
  $count = count($keys);
  
  $fd = fopen("keys.txt", 'w') or die("не удалось создать файл");
  
  for ($i = 0; $i < $count; $i++) {
    fwrite($fd, $keys[$i]."\n".$answer[$i]."\n");
  }
   

   fclose($fd);

   header('Location: http://bot.ru');    

 } //если была нажата кнопка  

?>