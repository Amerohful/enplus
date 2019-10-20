<?php session_start();?>
<!doctype html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport"
          content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <link href="https://fonts.googleapis.com/css?family=Montserrat&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="style/style.min.css">
    <title>Enot+</title>
</head>

<body>
<?php include 'header.php'?>

<main>
    <section class="top">
        <div class="left">
            <h2>ответы нового бота</h2>
            <nav class="bots-nav">
                <div class="bots-nav-item selected">новые ответы</div>
                <div class="bots-nav-item">шаблоны</div>
            </nav>
        </div>
    </section>
    <form class="commands-form" method="POST" action="download_keys/save_keys.php">
      <div class="form-control">
        <button type="button" name="button" class="btn add-scene-btn" onclick="addPair()">добавить сценарий</button>
        <button type="submit" name="ok" class="btn create-bot-btn">создать бота</button>
      </div>
        <div class="commands">
            <div class="pair">
              <p class="number">Сценарий № </p>
                <label>Ключ<textarea placeholder="через запятую" class="key-words"  name="key-words[]"></textarea></label>
                <label>Значение<textarea placeholder="ответ" class="answer" name="answer[]"></textarea></label>
            </div>
            <div class="pair template">
              <p class="number">Сценарий № </p>
              <label>Ключ<textarea placeholder="через запятую" class="key-words"  name="key-words[]"></textarea></label>
              <label>Значение<textarea placeholder="ответ" class="answer" name="answer[]"></textarea></label>
            </div>
        </div>

    </form>
</main>

<footer></footer>

<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
<script src="style/visual.js"></script>
</body>

</html>
