## Обозначение персонажей
define Rick = Character('Рик', color="#c19400")
define Morti = Character('Морти', color="#c19400")
define Kristi = Character('Кристина', color="#c19400")
define Kolya = Character('Коля', color="#c19400")
define Students = Character('Пара студентов', color="#c19400")
define Stas = Character('Стас', color="#c19400")

## Флаг
define relationshipWithKristina1 = False
define knowledgeAboutGameMechanics = False
define knowledgeAboutUlearn = False

## Среда разработки Новелы
label start:

    scene 1
    with fade
    Morti "Черт возьми, Рик! Куда мы попали?!"

    scene 2
    with fade
    Rick "Тише Морти, инопланетная тварь сломала мою телепортационную пушку, мы щас можем быть где угодно!"

    scene 3
    with fade
    Morti "О Рик! Кажется, эта вселенная населена совершенно обычными людьми"
    Rick "Ладно. Может быть, эта планета немного цивилизованней чем я ожидал"
    Rick "В любом случае нам нужно как можно скорее найти инструменты для починки портальной пушки, и сваливать с этого места"

    scene 4
    with fade 
    "Рик убирает пистолет"

    scene 5
    with fade
    Morti "Смотри тут кажется недалеко есть какой-то технический институт. Может быть, мы там найдем то, что нам нужно?"

    scene 6
    with fade
    Rick "Молодец, Морти. Пойдем посмотрим на технологии этого измерения"

    ## Scene 2

    scene 12
    with fade
    Rick "Ну хоть иногда бываешь полезен. Смотри может в этом месте и вправду будет что-нибудь полезное"
    
    ## Scene 3

    scene 13
    with fade
    "Рик и Морти идут по холлу ИРИТа"

    scene 23 
    with fade
    "Навстречу им идет неизвестная девушка"

    scene 33
    with fade
    "Морти спотыкается и роняет учебники девушки"

    scene 43
    with fade 
    Morti "Ой, изви..."
    "Смотрит на Кристину и впадает в состояние шока с красоты девушки"

    scene 53
    with fade 
    "Cреди упавших книг Морти видит открытый студенческий с именем Кристина"
    Morti "Кри-сти-на…"
    "Студентка подбирает свои учебники и убегает"

    scene 63
    with fade
    Rick "Мдаа…"
    Rick "Жизнь тебя ничему не учит"

    scene 73
    with fade
    Morti "Даже не думай"
    Rick "Послушай Морти я не хочу тебя расстраивать, но то, что люди называют любовью — это просто химическая реакция заставляющая людей размножаться"
    Rick "По началу это сильное чувство, Морти, но потом оно медленно слабеет, оставляя тебя в неудачном браке, прямо как у твоих родите…"
    Morti "ЗАТКНИСЬ!!!"

    scene 83
    with fade
    Rick "Как скажешь"
    Rick "Только потом не смей говорить о том, что я тебя не предупреждал"
    Morti "Чудак..."

    ## scene 4

    scene covok
    with fade 
    show rc and mr see
    with dissolve
    ""

    scene 24
    with fade
    Morti "Вау.."

    scene 34
    with fade
    show mr 34:
        yalign 1.0 xalign 0.2
    with dissolve
    Morti "Ура! Всегда хотел стать разработчиком игр!"

    show rc 34:
        yalign 3.6 xalign 1.0
    with dissolve
    "Рик неодобрительно смотрит на Морти"

    hide mr 34
    hide rc 34
    
    show rc and mr 35
    with dissolve
    Rick "О боже, Морти мы на неизвестной планете, за нами гонятся глобглобнавты, ты серьезно думаешь у нас есть время на твои хотелки?"
    Rick "Просто выиграем то, что нам надо на этом жалком конкурсе и свалим отсюда к чертовой матери"

    hide rc and mr 35

    show rc and mr 36
    with dissolve
    Morti "Погоди Рик, а как видеокарта поможет нам починить телепортационную пушку?"

    hide rc and mr 36

    show rc and mr 37
    with dissolve
    Rick "Твою мать, Морти, сколько раз я тебе объяснял, что в сердце пушки находится биологически сложная матрица телепортационного поля"
    Rick "Oснованная на комбинации миниатюрных червоточин, квантовых туннелей и розовых роботов, бьющихся с марсианскими пингвинами!"
    Rick "А внешне телепортационная пушка представляет собой изящное и сложное сочетание металла и электроники"

    hide rc and mr 37

    scene black1
    with fade
    ""
    scene 34
    with fade

    show rc 38:
        yalign 3.6 xalign 0.8
    with dissolve

    show mr 38:
        yalign -4.0 xalign 0.1
    with dissolve

    Rick "Владение таким устройством - равносильно неограниченной власти над пространством и временем и это всего лишь доля моей гениальности, Морти"
    Rick "И МЫ ПОТЕРЯЛИ ЕЕ ЛИШЬ ПОТОМУ, ЧТО ТЫ НЕ МОЖЕШЬ ДЕРЖАТЬ СВОЙ ГРЕБАННЫЙ РОТ ЗАКРЫТЫМ ПЕРЕД КУЧКОЙ ВООРУЖЕНЫХ УРОДЛИВЫХ КРЕТИНОВ"
    
    hide mr 38

    show mr 39:
        yalign 1.2 xalign 0.1
    with dissolve
    "Морти почти плачет..."
    Rick "Ладно, не ной, ты нас в дерьмо и похлеще ввязывал"

    hide mr 39
    hide rc 38

    show mr 40:
        yalign 1.7 xalign 0.5
    with dissolve
    Rick "Пойдем уже"

    hide mr 40
    
    ## Scene 5

    scene 15
    with fade 
    "Герои слушают диктора о конкурсе гейм-дизайнеров"

    scene 25
    with fade
    "Уважаемые участники! Добро пожаловать в великолепный мир разработки игр"
    "Сегодня мы собрались на этом  конкурсе, чтобы познакомиться с креативными умами и талантливыми разработчиками"
    "Вас ждет настоящий спектакль из творчества и инноваций. Участники этого конкурса представят свои гейм-дизайнерские проекты, в которых каждая деталь продумана до мельчайших подробностей"
    "Вы познакомитесь с удивительными персонажами, захватывающими сюжетами и интригующими геймплейными механиками"

    scene 35
    with fade
    show mr 34:
        yalign 1.0 xalign 0.2
    with dissolve
    show kristi:
        yalign 0.05 xalign 0.7
    with dissolve
    "Морти устает от речей диктора и погружается в свои мысли"

    hide mr 34
    hide kristi

    scene 45
    with fade 
    "Cпустя 10 минут мыслей о Кристине"
    "Участники конкурса, мы ждем ваших потрясающих презентаций и невероятных идей"
    "Покажите нам, что вы настоящие создатели миров, и дайте нам возможность попасть в ваши волшебные вселенные"

    scene 55
    with fade
    show mr 5_5:
        yalign 1.3 xalign 0.5
    Morti "А где Рик?"

    hide mr 5_5

    scene 655
    with fade
    show kolya 65:
        xalign 0.6
    with dissolve

    show stas 65:
        xalign 0.9
    with dissolve
    "Морти видит трёх студентов гейм-developer"
    Students "У меня есть идея для новой игры, что скажете?"
    Students "Давай, рассказывай свою идею"
    Students "Так вот, я думал о создании приключенческой игры в жанре фэнтези"
    Students "Мы можем создать удивительный мир с магией, эпическими сражениями и увлекательными головоломками…"

    hide stas 65
    hide kolya 65

    scene 655
    with fade
    show kolya 85:
        xalign 0.7
    with dissolve

    show stas 65:
        xalign 1.1
    with dissolve

    show mr 85:
        xalign 0.2 yalign 1.5
    with dissolve
    Morti "Привет ребят!"
    Morti "Можете рассказать о том, как выиграть в конкурсе"
    Kolya "Я вижу ты тут новенький, пекус что-ли?"
    Morti "Ммм… Да…"

    hide stas 65
    hide kolya 85
    hide mr 85

    scene 95
    with fade
    show mr 95:
        yalign 1.1 xalign -0.4
    with dissolve
    Kolya "Мы со Стасом собираемся в кафешку, здесь в радике. Пошли с нами, по дороге расскажу о конкурсе"

    hide mr 95

    ## Scene 6

    scene 16
    with fade
    "Ребята идут в ресторан"
    show kolya 16:
        xalign 0.15
    with dissolve
    show mr 16
    with dissolve
    Kolya "Ну так вот соревнование разбито на 5 этапов"
    show stas 16:
        xalign 0.9
    with dissolve
    Stas "Сюжет, дизайн, программная часть, звук и тестирование"
    Kolya "И на финальном этапе все конкурсанты представляют финальный билд игры"

    hide kolya 16
    hide mr 16
    hide stas 16

    scene 26
    with fade
    show mr 39:
        yalign 1.5 xalign 0.3
    with dissolve
    show stas 26:
        xalign 0.8
    Stas "Садись, мы щас быстро закажем"

    hide mr 39
    hide stas 26

    scene 36
    with fade
    show mr 36:
        yalign -0.2  xalign 0.48
    with dissolve
    "Морти сел за стол"

    hide mr 36

    scene 46
    with fade
    show kolya 46:
        xalign 0.3 yalign 1.1
    with dissolve
    show stas 46:
        xalign 0.7 yalign 1.9
    with dissolve
    ""

    hide kolya 46
    hide stas 46

    scene 56
    with fade
    show kr 56:
        xalign 0.8 yalign 1.1
    with dissolve
    "Морти видит плачущую Кристину..."
    show mr 56:
        xalign 0.2 yalign 1.7
    with dissolve
    Morti "Эй ты чего? Что случилось?"

    hide mr 56
    hide kr 56

    show mr 66:
        xalign 0.2 yalign 1.1
    with dissolve
    show kr 66:
        xalign 0.8 yalign 1.1
    Kristi "Я не могу решить практику на юлерне. Эти коллекции так достали меня..."
    Morti "Колл… Что?"

    hide mr 66
    hide kr 66

    show kr 76:
        xalign 0.8 yalign 1.1
    with dissolve
    show mr 39:
        yalign 1.5 xalign 0.2
    with dissolve
    Kristi "Ты не в теме?"
    Kristi "Все радисты которые учат сишарп учат его на юлерне."
    Kristi "Коллекция это одна из самых труднейших тем для понимания"

    hide mr 39
    hide kr 76

    "Коля подзывает Морти"

    show kolya 85:
        xalign 0.8
    with dissolve
    Kolya "Мы тут решили затусить вечером. Как раз будет возможность рассказать тебе еще о играх"
    show mr 86:
        xalign 0.2 yalign 1.1
    with dissolve
    menu:
        Kolya "Ты пойдешь?"

        "Помочь Кристине с Ulearn":
            $ relationshipWithKristina1 = True
            jump ulearn

        "Тусить с Колей":
            jump tusit
    return
    

label tusit:

    scene 56
    with fade
    show kolya 85:
        xalign 0.8
    with dissolve
    show mr 95:
        xalign -0.1 yalign 1.1
    with dissolve
    Morti "Да конечно! Пошли"
    
    hide mr 95
    hide kolya 85

    scene 162
    with fade
    show people 162:
        xalign 0.5 yalign -0.5
    with dissolve
    "Группа студентов" "Рассказывают разные истории"

    hide people 162

    scene 262
    with fade
    show mr 262:
        xalign 0.5 yalign -8.0
    with dissolve 
    "Морти решает пойти осмотреть квартиру"

    hide mr 262

    scene 362
    with fade
    show mr 362:
        xalign 0.8 yalign 1.1
    with dissolve
    "Морти заходит в комнату где Коля с Стасом решают практику “Коллекции” на Ulearn"

    hide mr 362

    scene 462
    with fade
    "Рядом лежит книга про игровые механики"

    scene 562
    with fade
    show mr 562:
        xalign 0.7 yalign 1.1
    with dissolve
    "Мысли Морти" "Кажется эта книга может помочь нам с Риком разработать игру"
    "Мысли Морти" "Но если пацаны объяснят мне эту практику, я смогу помочь Кристине..."

    menu:
        "Прочитать книгу про игровые механики":
            $ knowledgeAboutGameMechanics =True
            jump readBook
        
        "Попросить объяснить решение практики":
            $ knowledgeAboutUlearn = True
            jump help

        "Забить на все и расслабиться":
            jump chill

    


    return


label ulearn:

    scene 56
    with fade 
    show mr 161:
        xalign 0.2 yalign 1.1
    with dissolve
    Morti "Я наверное пас, мне там нужно еще своего деда найти..."
    show kolya 161:
        xalign 0.8 yalign 1.1
    with dissolve
    Kolya "Жаль конечно, но ладно, только добавь меня в ВК на случай если помощь нужна будет"

    hide mr 161
    hide kolya 161

    show mr 261:
        xalign 0.2 yalign 1.1
    with dissolve
    Morti "Куда?"
    show kolya 261:
        xalign 0.8
    with dissolve
    "Коля объясняет за местные социальные сети и они обмениваются контактами"

    hide kolya 261
    hide mr 261

    scene 361
    with fade
    show kolya 361:
        yalign 1.1 xalign 0.7
    with dissolve
    "Коля уходит"

    hide kolya 361

    scene 461
    with fade
    show kr 461:
        xalign 0.1 yalign 1.1
    with dissolve
    "Морти подходит к Кристине"
    show mr 461:
        yalign 1.5 xalign 0.9
    with dissolve 
    Morti "Не против вместе подумать над этой практикой?"
    Kristi "Давай"

    hide kr 461
    hide mr 461

    with fade
    show kr 561:
        xalign 0.1 yalign 1.1
    with dissolve
    show mr 561:
        yalign 1.5 xalign 0.9
    with dissolve 
    "Морти и Кристина вместе думают над задачами"

    scene 661
    with fade
    ""
    scene 461
    with fade
    show mr 761:
        xalign 1.0 yalign 1.1
    with dissolve
    Morti "Наконец-то, мы прошли все тесты"
    show kr 761:
        yalign -1.0 xalign 0.2
    with dissolve 
    Kristi "Осталось только дождаться код-ревью от препода"

    hide mr 761
    hide kr 761

    show mr 861:
        yalign 1.1 xalign 0.9
    with dissolve 
    Morti "Уже вечер. Ты не знаешь где можно здесь переночевать?"
    show kr 861:
        xalign 0.1 yalign 1.1
    with dissolve
    Kristi "Да, я живу в общежитии неподалеку, думаю сможем договориться пустить тебя"

    hide kr 861
    hide mr 861

    scene 961
    with fade
    show mr 961:
        yalign -100.0 xalign 0.5
    with dissolve 
    show kr 961:
        xalign 0.3 yalign 1.5
    with dissolve
    "Морти и Кристина идут к общежитию и видят Рика"

    hide kr 961
    hide mr 961

    scene 1061
    with fade
    show rc and mr 1061
    with dissolve
    Morti "Рик! Где тебя все это время носило?"
    Rick "Я добывал нам ордера, чтобы было где переночевать"
    Rick "Пошли в нашу комнату"

    jump sceneSeven

    return


## Прочитать книгу про игровые механики
label readBook:

    scene r 1
    with fade
    "Морти подбирает книгу и садиться читать ее"
    show mr r 1:
        xalign 0.7 yalign 1.1
    with dissolve
    "Морти несколько часов изучает книгу"

    "Проектирование игровых механик: Разработчик должен уметь составлять и балансировать различные механики, чтобы создать интересный и увлекательный игровой процесс"
    "Это включает в себя учет сложности, баланс между различными средствами, временем, затратами игрока и другими факторами"

    "Прототипирование: Знание игровых механик поможет разработчику создавать прототипы игровых систем, чтобы оценить их эффективность и работоспособность"
    "Это позволяет проверить идеи и модифицировать их до начала полноценной разработки"

    "Исправление ошибок и оптимизация: Разработчик, зная игровые механики, может легко идентифицировать и исправить возникающие проблемы в игре, такие как баги, неравновесие или неправильное функционирование систем"
    "Это помогает улучшить качество и играбельность игры"

    "Инновации: Знание игровых механик позволяет разработчикам экспериментировать, добавлять новые и оригинальные игровые элементы"
    "Это может привлечь новых игроков и сделать игру уникальной"

    hide mr r 1

    show mr r 2:
        xalign 0.7 yalign 1.1
    with dissolve
    Morti "Вау, полезная книга. Думаю с помощью Рика я смогу перенять пару механик из этой книги в нашу игру"

    hide mr r 2

    jump tusaEnd

    return


## Попросить объяснить решение практики
label help:
    
    scene h 1
    with fade
    "Морти подходит к парням"
    Morti "Парни можете помочь с предыдущей практикой?"
    Kolya "С коллекциями что-ли? Мы их сами наугад решили, но ладно давай попробуем"

    scene h 2
    with fade
    "Парни объясняют Морти решения задач"

    scene h 3
    with fade
    Morti "Кажется я понял, спасибо"
    Kolya "Ладно, парни уже поздно пора по домам"
    
    jump tusaEnd

    return


## Забить на все и расслабиться
label chill:

    scene c 1
    with fade 
    show mr c 1:
        xalign 0.2 yalign 1.1
    with dissolve
    show kolya c 1:
        xalign 0.9 yalign -1.0
    with dissolve
    "Морти и Коля разговаривают о чём-то"

    hide kolya c 1
    hide mr c 1

    show mr c 2:
        xalign 0.3 yalign 1.1
    with dissolve
    show kolya c 2:
        xalign 0.9 yalign 1.1
    with dissolve 
    Morti "Ха-ха-ха, интересное у вас измерение конечно"
    Kolya "Измерение? Ты о чем вообще?"

    hide kolya c 2
    hide mr c 2

    show mr c 3:
        xalign 0.3 yalign 1.1
    with dissolve
    show kolya c 3:
        xalign 0.9 yalign 1.1
    with dissolve 
    Morti "Да неважно, я просто устал. Где тут кстати туалет?"
    Kolya "В коридоре левая дверь"

    hide mr c 3
    hide kolya c 3

    scene c 4
    with fade
    show mr c 4:
        xalign 0.2 yalign 1.0
    with dissolve
    "Морти идет в туалет"
    show nn c 4:
        xalign 0.7 yalign 1.1
    with dissolve
    "У входа стоит подозрительный парень"
    "Тосщий парень" "Проходи"

    menu:
        "Пройти в туалет":
            jump tualet
            
        "Отказаться":
            jump otkaz

    return


label tusaEnd:

    scene 162
    with fade
    show people leave
    with dissolve
    "Тусовка заканчивается"

    hide people leave

    scene rhc 7
    with fade
    show mr r 7:
        xalign 0.8 yalign 1.1
    with dissolve
    show rc r 7:
        yalign 1.1 xalign 0.2
    with dissolve
    "Морти идет по профессорской, где встречает Рика"

    hide mr r 7
    hide rc r 7

    show rc and mr r 8
    with dissolve
    Morti "Где тебя черт возьми носило?"
    Rick "Тише Морти, я искал нам ночлег"

    hide rc and mr r 8

    scene rhc 9
    with fade
    show ssk:
        xalign 0.5 yalign 0.1
    with dissolve
    "Рик показывает два ордена с фотками Рика и Морти"

    hide ssk

    scene rhc 7
    with fade
    show rc and mr r 10
    with dissolve
    Morti "Боже Рик, где ты достал ордера? Неужели ты их подделал?!"
    Rick "Меньше вопросов, Морти. Пойдем осмотрим наш временный дом"

    hide rc and mr r 120

    scene 961
    with fade
    "Герои отправляются в общежитие"
    show rc and mr r 11
    with dissolve
    ""
    jump sceneSeven

    return


label tualet:

    scene ural
    with fade
    show mr t 6
    with dissolve
    "Морти решил довериться таинственному незнакомцу и на следующий день проснулся неизвестно где, без телефона и головной болью"

    hide mr t 6

    scene black
    with fade
    "Конец.."

    return


label otkaz:

    scene c 1
    with fade
    "Морти возвращается к Коле"
    show t 1:
        xalign 0.2 yalign 1.0
    with dissolve
    Morti "Что это за странный тип около туалета?"
    show kolya 85:
        xalign 0.8
    with dissolve
    Kolya "Не знаю, в любом случае, пора идти по домам"

    hide kolya 85

    show kolya c 1:
        xalign 1.1
    with dissolve
    Kolya "Ты где живешь, кстати?"

    hide t1

    show t 2:
        xalign 0.2 yalign 1.0
    with dissolve
    Morti "Да на самом деле нигде, не знаешь где здесь можно переночевать?"
    Kolya "Да конечно, я живу в одном из общежитий, думаю смогу тебе помочь"

    hide t 2
    hide kolya c 1

    scene rhc 7
    with fade
    show mr t 3:
        xalign 0.6 yalign 1.1
    with dissolve
    show kolya t 3:
        xalign 0.9 yalign 1.1
    with dissolve
    "Морти и Коля идут по профессорской где видят Рика"
    show rc t 3:
        xalign 0.1 yalign 1.1
    with dissolve
    ""

    hide kolya t 3
    hide rc t 3
    hide mr t 3

    show rc r 7:
        xalign 0.3 yalign 1.0
    with dissolve
    show kolya 161:
        xalign 0.9 yalign 1.1
    with dissolve
    show mr t 4:
        xalign 0.6 yalign 1.1
    with dissolve
    Morti "Знакомься Коль это мой дед Рик"
    Morti "Коля поможет нам с жильем"

    hide kolya 161

    show kolya t 5:
        xalign 0.95 yalign 1.1
    with dissolve
    Kolya "Здравствуйте, пойдемте с нами я найду вам в комнату в общежитии"

    hide kolya t 5
    hide mr t 4
    hide rc r 7

    scene 961
    with fade
    show t 6
    with dissolve
    ""

    jump sceneSeven

    return


## Scene 7
label sceneSeven:

    scene 17
    with fade
    show rc and mr see
    with dissolve
    "Герои осматривают комнату"

    hide rc and mr see

    show rc 34:
        xalign 0.7 yalign 1.1
    with dissolve
    Rick "Ну в целом неплохо"

    hide rc 34

    show rc and mr 35:
        xalign 0.5 yalign 1.1
    with dissolve
    Morti "Неплохо? Где тебя черт возьми носило?"

    hide rc and mr 35

    show rc and mr 1061
    with dissolve
    Rick "Я познакомился с писателем, вроде толковый мужик"
    Rick "Мы должны сегодня встретиться с ним в баре, где он мне пообещал помочь с сюжетом, взамен на кристаллы смерти"
    Rick "Ну а ты? Сделал хоть что-нибудь?"

    hide rc and mr 1061

    show mr 561:
        xalign 0.3 yalign 1.1
    with dissolve
    show rc 57:
        xalign 0.7 yalign 1.1
    with dissolve
    "Мысли Морти" "Черт! Нужно что-то ответить Рику, иначе опять будет гнать на меня что я бесполезный"

    hide rc 57
    hide mr 561

    if knowledgeAboutUlearn:

        scene 171
        with fade
        show nout:
            xalign 0.8 yalign 0.3
        with dissolve
        show mr 171:
            xalign 0.3 yalign 1.1
        with dissolve
        "Мысли Морти" "Точно, я видел у Кристины на ноутбуке приложения для дизайна!"

        hide mr 171
        hide nout

        scene 17
        with fade
        show mr c 2:
            xalign 0.3 yalign 1.1
        with dissolve
        Morti "Да, я думаю я решил проблему с дизайном для нашей игры"


    if knowledgeAboutGameMechanics:

        show mr 172:
            xalign 0.3 yalign 1.1
        with dissolve
        show rc 38:
            xalign 0.8 yalign 1.1
        with dissolve
        Morti "Да, я изучил книгу про игровые механики"
        Morti "Я ее немного почитал, думаю будет полезно для нас"



    




    return