<!doctype html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <title>"ENot+" - создай своего бота</title>
    <link rel="stylesheet" href="./style/style.css">
</head>


<body>

<?php

require_once 'connection.php';
$link = mysqli_connect($host, $user, $pass, $db, $port)
    or die(mysqli_error($link));

mysqli_close($link);
?>

    <div id="constructor">
        <nav class="side-menu">
            <a href="#" class="side-menu-item" data-item-name="reg" onclick="sideMenuItemClick(this)">1</a>
            <a href="#" class="side-menu-item" data-item-name="main" onclick="sideMenuItemClick(this)">2</a>
            <a href="#" class="side-menu-item" data-item-name="options" onclick="sideMenuItemClick(this)">3</a>

            <a href="#" class="side-menu-item" style='background: #0a0;'data-item-name="notmain" onclick="alert('that is your bot')">V</a>
        </nav>
        <main id="main">
            <section data-section-name="reg">
                <h2>контактные данные</h2>
                <div class="container">
                    <label>организация</label>
                    <input type="text" placeholder="EN+">

                    <label>ответственное лицо</label>
                    <input type="text" placeholder="имя, фамилия">

                    <label>почта</label>
                    <input type="text" placeholder="e-mail">

                    <label>телефон</label>
                    <input type="text" placeholder="номер телефона">
                </div>
            </section>
            <section data-section-name="main" class="hidden">
                <h2>основное</h2>
                <div class="container">
                    <label>название бота</label>
                    <input type="text" placeholder="MyVeryOwnBot">

                    <label>приветствие</label>
                    <textarea type="text" placeholder="hello World!"></textarea>

                    <label>назначение</label>
                    <form action="">
                        <input type="checkbox" id="clients" name="dest">
                        <label for="clients">работа с клиентами</label>

                        <input type="checkbox" id="req">
                        <label for="req">подача заявок</label><br>

                        <input type="checkbox" id="1s" name="dest">
                        <label for="1s">работа с документацией</label><br>
                    </form>

                    <label>платформы</label>
                    <form action="">
                        <label for="platfotm-tlgr">
                            <input type="checkbox" id="platfotm-tlgr" class="chck-platform">
                            telegram
                        </label>
                        <input type="text" placeholder="token">
                        <br>

                        <input type="checkbox" id="platform-whapp" class="chck-platform" disabled>
                        <label for="platform-whapp">whatsapp</label>
                        <input type="text" placeholder="token" disabled>
                        <br>

                        <input type="checkbox" id="platform-viber" class="chck-platform" disabled>
                        <label for="platform-viber">viber</label>
                        <input type="text" placeholder="token" disabled>
                        <br>

                        <input type="checkbox" id="platform-vidget" class="chck-platform" disabled>
                        <label for="platform-vidget">виджет на сайт</label>
                    </form>
                </div>
            </section>
            <section data-section-name="options" class="hidden">
                <h2>сценарии</h2>

                <div class="container" id="scenarios">
                    <textarea type="text" placeholder="ключи через запятую" class="scenario-keys template-k"></textarea>
                    <textarea type="text" placeholder="ответ" class="scenario-ans template-a"></textarea>
                </div>
                <a href="#" onclick="" class="button">добавить сценарий</a>
            </section>
        </main>
    </div>


</body>
</html>