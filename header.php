<header>
        <a href="index.php"><div class="logo">logo</div></a>
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
            <?php if(empty($_SESSION['login'])) { echo "<ul class=\"user-block\"><li><button class=\"auth-btn btn\" id='auth'>вход</button></li>
            <li><button class=\"reg-btn btn\">регистрация</button></li></ul>";}
            ?>
            <?php if(!empty($_SESSION['login'])) { echo "<ul class=\"user-block\"><li><form name='disconect' class=\"disconect-form\" action='disconect.php' method='post'><button class=\"btn auth\" type=\"submit\">Выход</button></form></li></ul>";}
            ?>
<!--            <button class="auth-btn btn">Войти</button>-->
        </div>
        
    </header>
