<header>
    <ul>
        <li class="current">1</li>
        <li class="">2</li>
        <li class="">3</li>
        <li class="last"><div class="container">.</div></li>
    </ul>
</header>


<main>
<!--    <form action="../db_processing/write_step_1.php" class="container" method="post">-->
    <form action="../index.php?step=2" class="container" method="post">
        <h1>контактные данные</h1>

        <label for="">Название организации</label>
        <input type="text" name='org' class="c-r" placeholder="En+">

        <label for="">Полное имя ответственного</label>
        <input type="text" name='fullName'class="c-r" placeholder="Иванов Василий Петрович">

        <label for="">Почта</label>
        <input type="text" name="email" class="c-r" placeholder="e-mail">

        <label for="">Телефон</label>
        <input type="text" name="mobile" class="c-r" placeholder="+X-(XXX)-XXX-XX-XX">

        <input type="submit" value="далее">
    </form>
</main>