<?php session_start();?>
<!doctype html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport"
          content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <link href="https://fonts.googleapis.com/css?family=Montserrat&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="style/style.css">
    <title>БиБот+</title>
</head>
<body>
    <header>
        <div class="logo">logo</div>
        <nav class="main-nav">
            <div class="main-nav-item">боты</div>
            <div class="main-nav-item">инструкция</div>
            <div class="main-nav-item">поддержка</div>
        </nav>
        <div class="place-holder"></div>
        <div class="user-auth-info">
            <?php echo $_COOKIE['login'];
            ?>
            <p><?php if(!empty($_SESSION['login'])){echo $_SESSION['login'];} ?></p>
            <?php if(empty($_SESSION['login'])) { echo "<ul class=\"user-block\"><li><button class=\"auth-btn btn\" id='auth'>Вход</button></li>
            <li><button class=\"reg-btn btn\">Регистрация</button></li></ul>";}
            ?>
            <?php if(!empty($_SESSION['login'])) { echo "<ul class=\"user-block\"><li><form name='disconect' class=\"disconect-form\" action='disconect.php' method='post'><button class=\"btn auth\" type=\"submit\">Выход</button></form></li></ul>";}
            ?>
<!--            <button class="auth-btn btn">Войти</button>-->
        </div>
    </header>
    <main>
        <section class="top">
            <div class="left">
                <h2>мои боты</h2>
                <nav class="bots-nav">
                    <div class="bots-nav-item selected">созданные</div>
                    <div class="bots-nav-item">шаблоны</div>
                </nav>
            </div>
            <a href='#' class="create-new-btn btn">новый бот</a>
        </section>
        <section class="messenger">
            <h2>telegram</h2>
            <div class="bots">
                <div class="bot">
                    <h4 class="bot-name">test name</h4>
                    <p class="bot-description"></p>
                </div>
            </div>
        </section>
        <section class="messenger">
            <h2>viber</h2>
            <div class="bots"></div>
        </section>
        <section class="messenger">
            <h2>whatsapp</h2>
            <div class="bots"></div>
        </section>
    </main>

    <footer>
    </footer>


    <section class="auth-block pop-up">
        <form method="POST" action="auth/auth.php">
            <label for="login">Логин</label>
            <input type="text" name="login" id="login">
            <label for="password">Пароль</label>
            <input type="password" name="password" id="password">
            <button type="submit">Войти</button>
        </form>
    </section>
    <section class="reg-block pop-up">
    <form class="reg-form" method="post" action="registration/regScript.php" id="regForm">
      <h2>Форма регистрации</h2>
      <p>Заполните все поля!</p>
        <label for="reg-login">Логин</label><input type="text" name="reg-login" id="reg-login">
        <label for="reg-password">Пароль</label><p class="tiny">*Должен содержать 5 знаков и более</p><input type="password" name="reg-password" id="reg-password">
        <label for="repeat-password">Повторите пароль</label><input type="password" name="repeat-password" id="repeat-password">
        <label for='reg-email'>Почта</label><input type="text" name="reg-email" id='reg-email'>
        <label for='reg-accord'>Согласие</label><input type="radio" name="accord"  id='reg-accord'>
        <div class="footer-reg">
        <a class="btn back-link" href="index.php">На главную</a>
        <button class="btn reg-submit" type="submit" name="go">Ок</button>
        </div>
      </form>
  </section>
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
    <script src="style/visual.js"></script>
</body>
</html>