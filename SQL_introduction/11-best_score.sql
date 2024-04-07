-- tache 10
-- liste selon un objectif défini

SELECT score, name
    FROM second_table
    WHERE score >= 10
    ORDER BY score DESC;