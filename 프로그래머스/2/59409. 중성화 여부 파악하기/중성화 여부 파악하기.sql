-- 코드를 입력하세요
SELECT ANIMAL_ID, NAME,
       CASE WHEN SEX_UPON_INTAKE LIKE 'Neutered%' then 'O'
            WHEN SEX_UPON_INTAKE LIKE 'Spayed%' then 'O'
            ELSE 'X' END AS '중성화'
FROM ANIMAL_INS
WHERE SEX_UPON_INTAKE IS NOT NULL
ORDER BY ANIMAL_ID