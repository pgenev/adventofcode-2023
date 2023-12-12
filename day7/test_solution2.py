import pytest
from solution_part2 import transform_joker

@pytest.mark.parametrize(
    "card, expected_hand", [
        ("3632J", "Three of a kind"),
        ("9J656", "Three of a kind"),
        ("AK9J8", "One pair"),
        ("6JQ9J", "Three of a kind"),
        ("47JT6", "One pair"),
        ("6J554", "Three of a kind"),
        ("KJAKA", "Full house"),
        ("6JTJJ", "Four of a kind"),
        ("2626J", "Full house"),
        ("55J27", "Three of a kind"),
        ("J383K", "Three of a kind"),
        ("4Q89J", "One pair"),
        ("5A5AJ", "Full house"),
        ("88AJJ", "Four of a kind"),
        ("QJ725", "One pair"),
        ("8T9JT", "Three of a kind"),
        ("JQAQ5", "Three of a kind"),
        ("TTTJT", "Five of a kind"),
        ("JKKKK", "Five of a kind"),
        ("AJ552", "Three of a kind"),
        ("7J969", "Three of a kind"),
        ("4Q4JJ", "Four of a kind"),
        ("6J757", "Three of a kind"),
        ("Q5J2A", "One pair"),
        ("JTK7K", "Three of a kind"),
        ("6JQ45", "One pair"),
        ("QQQJQ", "Five of a kind"),
        ("5858J", "Full house"),
        ("QJ866", "Three of a kind"),
        ("48J43", "Three of a kind"),
        ("2Q4J7", "One pair"),
        ("T3TJK", "Three of a kind"),
        ("2836J", "One pair"),
        ("J3QQ8", "Three of a kind"),
        ("AJ533", "Three of a kind"),
        ("3TT4J", "Three of a kind"),
        ("J6282", "Three of a kind"),
        ("J8K84", "Three of a kind"),
        ("38J53", "Three of a kind"),
        ("3978J", "One pair"),
        ("39K6J", "One pair"),
        ("8428J", "Three of a kind"),
        ("TJ4T7", "Three of a kind"),
        ("6J434", "Three of a kind"),
        ("8KTTJ", "Three of a kind"),
        ("QQJ36", "Three of a kind"),
        ("J6KA5", "One pair"),
        ("JQ994", "Three of a kind"),
        ("J277T", "Three of a kind"),
        ("98J29", "Three of a kind"),
        ("JT5TQ", "Three of a kind"),
        ("3QTJ3", "Three of a kind"),
        ("JK3T3", "Three of a kind"),
        ("7379J", "Three of a kind"),
        ("K5J25", "Three of a kind"),
        ("9746J", "One pair"),
        ("9J9J6", "Four of a kind"),
        ("562J9", "One pair"),
        ("J5TT5", "Full house"),
        ("QAAJ8", "Three of a kind"),
        ("797J9", "Full house"),
        ("59J64", "One pair"),
        ("9J4KK", "Three of a kind"),
        ("9986J", "Three of a kind"),
        ("786J7", "Three of a kind"),
        ("5J555", "Five of a kind"),
        ("QTJQK", "Three of a kind"),
        ("32J37", "Three of a kind"),
        ("9J77J", "Four of a kind"),
        ("K9J9K", "Full house"),
        ("5J88J", "Four of a kind"),
        ("6Q6J3", "Three of a kind"),
        ("9QQJ9", "Full house"),
        ("JJTA2", "Three of a kind"),
        ("455J8", "Three of a kind"),
        ("477JT", "Three of a kind"),
        ("2739J", "One pair"),
        ("7J7J3", "Four of a kind"),
        ("6QA2J", "One pair"),
        ("TJ53A", "One pair"),
        ("9999J", "Five of a kind"),
        ("8J62A", "One pair"),
        ("5J2JQ", "Three of a kind"),
        ("Q6QJK", "Three of a kind"),
        ("4JT59", "One pair"),
        ("KTJQJ", "Three of a kind"),
        ("AJ2KK", "Three of a kind"),
        ("85J75", "Three of a kind"),
        ("639J2", "One pair"),
        ("KJ973", "One pair"),
        ("3A46J", "One pair"),
        ("QJK65", "One pair"),
        ("QK67J", "One pair"),
        ("4A4JA", "Full house"),
        ("TA5J9", "One pair"),
        ("6J666", "Five of a kind"),
        ("6J677", "Full house"),
        ("AJK83", "One pair"),
        ("AJT8J", "Three of a kind"),
        ("T2T8J", "Three of a kind"),
        ("J4524", "Three of a kind"),
        ("KJ4AA", "Three of a kind"),
        ("J9696", "Full house"),
        ("J28K2", "Three of a kind"),
        ("AQ8TJ", "One pair"),
        ("8A9JA", "Three of a kind"),
        ("24J25", "Three of a kind"),
        ("J7J87", "Four of a kind"),
        ("3J366", "Full house"),
        ("7JK9J", "Three of a kind"),
        ("855J3", "Three of a kind"),
        ("2T44J", "Three of a kind"),
        ("JJJ8J", "Five of a kind"),
        ("2J827", "Three of a kind"),
        ("J2828", "Full house"),
        ("JJ369", "Three of a kind"),
        ("J2962", "Three of a kind"),
        ("K7A7J", "Three of a kind"),
        ("9J93T", "Three of a kind"),
        ("JJJJJ", "Five of a kind"),
        ("JJJ2J", "Five of a kind"),
        ("JAAAA", "Five of a kind"),
        ("J9A5A", "Three of a kind"),
        ("J3333", "Five of a kind"),
        ("TJ986", "One pair"),
        ("56J4T", "One pair"),
        ("967J7", "Three of a kind"),
        ("JQQ33", "Full house"),
        ("JJ852", "Three of a kind"),
        ("K4J4T", "Three of a kind"),
        ("K6JQ6", "Three of a kind"),
        ("JTT22", "Full house"),
        ("2J64A", "One pair"),
        ("AJJQ7", "Three of a kind"),
        ("6T75J", "One pair"),
        ("J323A", "Three of a kind"),
        ("JJ833", "Four of a kind"),
        ("J24TJ", "Three of a kind"),
        ("362QJ", "One pair"),
        ("2JT43", "One pair"),
        ("438J5", "One pair"),
        ("TJ6T7", "Three of a kind"),
        ("T6TJ6", "Full house"),
        ("QJ82J", "Three of a kind"),
        ("2J992", "Full house"),
        ("J2442", "Full house"),
        ("39J37", "Three of a kind"),
        ("TK3J6", "One pair"),
        ("J5T95", "Three of a kind"),
        ("J4444", "Five of a kind"),
        ("JK46T", "One pair"),
        ("JK794", "One pair"),
        ("4J545", "Full house"),
        ("864J9", "One pair"),
        ("4QJQT", "Three of a kind"),
        ("644QJ", "Three of a kind"),
        ("T3JA9", "One pair"),
        ("J4JQ5", "Three of a kind"),
        ("KJJA5", "Three of a kind"),
        ("Q7AJ3", "One pair"),
        ("K4KTJ", "Three of a kind"),
        ("4JAT8", "One pair"),
        ("3J656", "Three of a kind"),
        ("J3289", "One pair"),
        ("J5A9J", "Three of a kind"),
        ("K55KJ", "Full house"),
        ("J26K3", "One pair"),
        ("2AJK9", "One pair"),
        ("T4JJT", "Four of a kind"),
        ("KJ945", "One pair"),
        ("JAA88", "Full house"),
        ("T2JT4", "Three of a kind"),
        ("7J447", "Full house"),
        ("8QJ8A", "Three of a kind"),
        ("J33JQ", "Four of a kind"),
        ("8888J", "Five of a kind"),
        ("9T9JJ", "Four of a kind"),
        ("T7QJ7", "Three of a kind"),
        ("KJ746", "One pair"),
        ("2TJJ2", "Four of a kind"),
        ("J88JT", "Four of a kind"),
        ("92A9J", "Three of a kind"),
        ("9J488", "Three of a kind"),
        ("AJ979", "Three of a kind"),
        ("8T3J8", "Three of a kind"),
        ("J87Q3", "One pair"),
        ("9J2TQ", "One pair"),
        ("KA6QJ", "One pair"),
        ("622JT", "Three of a kind"),
        ("6KJK6", "Full house"),
        ("KJA3K", "Three of a kind"),
        ("A4J86", "One pair"),
        ("T8QJ8", "Three of a kind"),
        ("9J978", "Three of a kind"),
        ("TJ92A", "One pair"),
        ("JK6JK", "Four of a kind"),
        ("J75A7", "Three of a kind"),
        ("JK3K3", "Full house"),
        ("773J5", "Three of a kind"),
        ("TK8JA", "One pair"),
        ("Q59QJ", "Three of a kind"),
        ("JA66A", "Full house"),
        ("A87JK", "One pair"),
        ("7777J", "Five of a kind"),
        ("2222J", "Five of a kind"),
        ("Q4J4Q", "Full house"),
        ("JT2A2", "Three of a kind"),
        ("J55JA", "Four of a kind"),
        ("J3773", "Full house"),
        ("9Q77J", "Three of a kind"),
        ("7QJQ7", "Full house"),
        ("69AJ6", "Three of a kind"),
        ("TQ59J", "One pair"),
        ("6TQJ4", "One pair"),
        ("J7AQ5", "One pair"),
        ("JQ8TT", "Three of a kind"),
        ("2Q96J", "One pair"),
        ("K44J5", "Three of a kind"),
        ("J233T", "Three of a kind"),
        ("4T5JA", "One pair"),
        ("A3JA3", "Full house"),
        ("JJQQA", "Four of a kind"),
        ("A6J55", "Three of a kind"),
        ("3A44J", "Three of a kind"),
        ("659JK", "One pair"),
        ("JQ642", "One pair"),
        ("JQA3K", "One pair"),
        ("87TQJ", "One pair"),
        ("AJQA9", "Three of a kind"),
        ("6JA99", "Three of a kind"),
        ("K5JQQ", "Three of a kind"),
        ("8K89J", "Three of a kind"),
        ("A6AJQ", "Three of a kind"),
        ("J7JT7", "Four of a kind"),
        ("5282J", "Three of a kind"),
        ("9KJ75", "One pair"),
        ("AJKQ5", "One pair"),
        ("7454J", "Three of a kind"),
        ("432AJ", "One pair"),
        ("6TT2J", "Three of a kind"),
        ("4J9K2", "One pair"),
        ("T4J28", "One pair"),
        ("4JJ48", "Four of a kind"),
        ("9K5JK", "Three of a kind"),
        ("6Q5J3", "One pair"),
        ("AJT6J", "Three of a kind"),
        ("66JKJ", "Four of a kind"),
        ("992JK", "Three of a kind"),
        ("8J638", "Three of a kind"),
        ("4Q66J", "Three of a kind"),
        ("3449J", "Three of a kind"),
        ("JA428", "One pair"),
        ("8J957", "One pair"),
        ("AAQAJ", "Four of a kind"),
        ('9J9A9', "Four of a kind"),
        ('T555J', "Four of a kind"),
        ('66JJ6', "Five of a kind"),
        ('J4555', "Four of a kind"),
        ('Q777J', "Four of a kind"),
        ('JJJQQ', "Five of a kind"),
        ('644J4', "Four of a kind"),
        ('JA555', "Four of a kind"),
        ('QQQ3J', "Four of a kind"),
        ('J7444', "Four of a kind"),
        ('6AAAJ', "Four of a kind"),
        ('99K9J', "Four of a kind"),
        ('J2262', "Four of a kind"),
        ('866J6', "Four of a kind"),
        ('J99J9', "Five of a kind"),
        ('333TJ', "Four of a kind"),
        ('9777J', "Four of a kind"),
        ('JJ4J4', "Five of a kind"),
        ('2J2J2', "Five of a kind"),
        ('222AJ', "Four of a kind"),
        ('949J9', "Four of a kind"),
        ('JKJKK', "Five of a kind"),
        ('6T6J6', "Four of a kind"),
        ('7J775', "Four of a kind"),
        ('JJQQQ', "Five of a kind"),
        ('6K6J6', "Four of a kind"),
        ('8J777', "Four of a kind"),
        ('33AJ3', "Four of a kind"),
        ('JA7AA', "Four of a kind"),
        ('JKK7K', "Four of a kind"),
        ('999JT', "Four of a kind"),
        ('TTTJJ', "Five of a kind"),
        ('8828J', "Four of a kind"),
        ('6JA66', "Four of a kind"),
        ('9J99Q', "Four of a kind"),
        ('J8838', "Four of a kind"),
        ('3J3J3', "Five of a kind"),
        ('J7333', "Four of a kind"),
        ('44J84', "Four of a kind"),
        ('AJ4AA', "Four of a kind"),
        ('7J77K', "Four of a kind"),
        ('7TJ77', "Four of a kind"),
        ('KJKQK', "Four of a kind"),
        ('J3335', "Four of a kind"),
        ('JKKTK', "Four of a kind"),
        ('JJ77J', "Five of a kind"),
        ('8AAJA', "Four of a kind"),
        ('656J6', "Four of a kind"),
        ('3QJ33', "Four of a kind"),
        ('J3433', "Four of a kind"),
        ('77J7J', "Five of a kind"),
        ('J8TTT', "Four of a kind"),
        ('JAJAA', "Five of a kind"),
        ('6J766', "Four of a kind"),
        ('J88J8', "Five of a kind"),
        ('T4JTT', "Four of a kind"),
        ('9444J', "Four of a kind"),
        ('555J6', "Four of a kind"),
        ('4J4J4', "Five of a kind"),
        ('8J8T8', "Four of a kind"),
        ('39J99', "Four of a kind"),
        ('J3KKK', "Four of a kind"),
        ('J5955', "Four of a kind"),
        ('KK9KJ', "Four of a kind"),
        ('J8898', "Four of a kind"),
        ('5J558', "Four of a kind"),
        ('JQ4QQ', "Four of a kind"),
        ('J55J5', "Five of a kind"),
        ('KKAJK', "Four of a kind")
    ]
)
def test_transform_joker(card, expected_hand):
    assert transform_joker(card) == expected_hand
