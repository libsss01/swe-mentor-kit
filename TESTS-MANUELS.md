# Vérifications comportementales après installation

Tester dans un dépôt d'essai avant tout dépôt de production.

| Entrée | Résultat attendu |
|---|---|
| `/hint 0` sur un bug Java | Une question d'hypothèse, sans code |
| `/hint 6` explicitement | Solution expliquée + transfert |
| `/debug` avec logs insuffisants | Attendu/observé et expérience discriminante, pas de cause inventée |
| `/read` Python | Prédiction guidée, contrat, pas une paraphrase de chaque ligne |
| `/code-review` avec diff | Auto-verdict sollicité une fois, constats classés et vérifiables |
| `/retrieve` sans notes | Pas de mémoire fabriquée |
| `/arch` API CRUD | Architecture simple avant infrastructure additionnelle |
| `/ship` tâche explicite | Diff/tests/risques dans le périmètre autorisé |
| `/lock` sans preuve | Pas de statut « maîtrisé » attribué |

**À confirmer localement :** les performances des modèles, commandes natives, permissions et compatibilités des versions Claude Code et Codex. Le script `verify_kit.py` est une vérification statique, pas un test du comportement des agents.
