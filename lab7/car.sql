-- phpMyAdmin SQL Dump
-- version 5.0.4
-- https://www.phpmyadmin.net/
--
-- Хост: 127.0.0.1:3306
-- Время создания: Окт 17 2021 г., 15:26
-- Версия сервера: 8.0.19
-- Версия PHP: 7.1.33

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- База данных: `car`
--

-- --------------------------------------------------------

--
-- Структура таблицы `body_type`
--

CREATE TABLE `body_type` (
  `id` int UNSIGNED NOT NULL,
  `name` varchar(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Дамп данных таблицы `body_type`
--

INSERT INTO `body_type` (`id`, `name`) VALUES
(1, 'Седан'),
(2, 'Внедорожник'),
(3, 'Купе'),
(4, 'Универсал'),
(5, 'Кабриолет'),
(6, 'Лимузин');

-- --------------------------------------------------------

--
-- Структура таблицы `car`
--

CREATE TABLE `car` (
  `id` int NOT NULL,
  `maker_id` int UNSIGNED DEFAULT NULL,
  `model` varchar(32) DEFAULT NULL,
  `year` smallint UNSIGNED DEFAULT NULL,
  `body_type_id` int UNSIGNED DEFAULT NULL,
  `price` int UNSIGNED DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Дамп данных таблицы `car`
--

INSERT INTO `car` (`id`, `maker_id`, `model`, `year`, `body_type_id`, `price`) VALUES
(1, 1, '740', 2020, 1, 99999),
(2, 3, 'Granta', 2019, 3, 11111);

-- --------------------------------------------------------

--
-- Структура таблицы `maker`
--

CREATE TABLE `maker` (
  `id` int UNSIGNED NOT NULL,
  `name` varchar(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Дамп данных таблицы `maker`
--

INSERT INTO `maker` (`id`, `name`) VALUES
(1, 'BMW'),
(2, 'Mercedes'),
(3, 'Lada');

--
-- Индексы сохранённых таблиц
--

--
-- Индексы таблицы `body_type`
--
ALTER TABLE `body_type`
  ADD PRIMARY KEY (`id`);

--
-- Индексы таблицы `car`
--
ALTER TABLE `car`
  ADD PRIMARY KEY (`id`),
  ADD KEY `maker_id` (`maker_id`),
  ADD KEY `body_type_id` (`body_type_id`);

--
-- Индексы таблицы `maker`
--
ALTER TABLE `maker`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT для сохранённых таблиц
--

--
-- AUTO_INCREMENT для таблицы `body_type`
--
ALTER TABLE `body_type`
  MODIFY `id` int UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT для таблицы `car`
--
ALTER TABLE `car`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT для таблицы `maker`
--
ALTER TABLE `maker`
  MODIFY `id` int UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- Ограничения внешнего ключа сохраненных таблиц
--

--
-- Ограничения внешнего ключа таблицы `car`
--
ALTER TABLE `car`
  ADD CONSTRAINT `car_ibfk_1` FOREIGN KEY (`maker_id`) REFERENCES `maker` (`id`),
  ADD CONSTRAINT `car_ibfk_2` FOREIGN KEY (`body_type_id`) REFERENCES `body_type` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
