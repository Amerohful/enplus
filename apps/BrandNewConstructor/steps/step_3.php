<header>
    <ul>
        <li class="">1</li>
        <li class="">2</li>
        <li class="current">3</li>
        <li class="last"><div class="container">.</div></li>
    </ul>
</header>


<main>
    <form action="../index.php?step=4" class="container" method="post">
        <h1>настройка сценариев</h1>

        <textarea class="c-r quest-template"
                  placeholder="Вопрос"
                  rows="3"
                  name="questions[]"
                  id="quest-template"></textarea>

        <textarea class="c-r "
                  placeholder="Ответ"
                  rows="3"
                  name="answers[]"
                  id="ans-template"></textarea>

        <a href="#" onclick="addScenario(this)" class="last-page-left-btn">добавить</a>
        <input type="submit" value="завершить" class="last-page-right-btn">
    </form>
    <script src="script.js"></script>
<!--    as-->

</main>