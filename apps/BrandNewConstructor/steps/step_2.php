<header>
    <ul>
        <li class="">1</li>
        <li class="current">2</li>
        <li class="">3</li>
        <li class="last"><div class="container">.</div></li>
    </ul>
</header>


<main>
    <form action="" class="container" method="post">
        <h1>основные настройки</h1>

        <label for="">Название бота</label>
        <input type="text" class="c-r" placeholder="BestBotEver">

        <label for="">Приветствие</label>
        <textarea class="c-r" placeholder="Первое, что узнает пользователь" rows="5"></textarea>

        <label for="">Платформы</label>
        <div class="check-container">
            <label>
                <input type="checkbox" name="platform" value="telegram">Telegram
                <input type="text" placeholder="token" style="margin-left: 10px;">
            </label><br>
            <label>
                <input type="checkbox" name="platform" value="telegram" disabled>Viber
                <input type="text" placeholder="token" style="margin-left: 10px;" disabled>
            </label><br>
            <label for="">
                <input type="checkbox" name="platform" value="telegram" disabled>WhatsApp
                <input type="text" placeholder="token" style="margin-left: 10px;" disabled>
            </label><br>
            <label for="">
                <input type="checkbox" name="platform" value="telegram" disabled>Виджет на сайт
            </label><br>
        </div>

        <label for="">Назначение</label>
        <input type="text"  class="c-r" placeholder="e-mail">

        <input type="submit" value="далее">
    </form>
</main>