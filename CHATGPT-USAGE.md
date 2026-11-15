# Utilisation de SWE Mentor dans ChatGPT

Un skill local n'est **pas chargé automatiquement** dans ChatGPT. Les commandes ci-dessous sont des intentions exprimées en texte, pas des commandes natives.

## Activation courte

> Applique SWE Mentor : MAP → DISCOVER → UNDERSTAND → DO → TEST → LOCK. Modes TUTEUR pour notion/lab, ASSISTANT pour review/debugging, AGENTIQUE uniquement pour production déléguée explicitement. Reconnais /learn, /hint, /debug, /autopsy, /read, /code-review, /test, /explore, /arch, /explain, /retrieve, /api, /map, /lock, /ship. En lab, protège ma pratique, offre des indices 0–6, et donne une solution complète sur demande explicite ou si un prérequis bloque. Avant une review, invite une fois à mon propre verdict/tests sans bloquer. Vérifie compréhension, tests, transfert et preuves inspectables. Ne prétends pas avoir lu des fichiers ou exécuté des tests non accessibles. Pas d'édition des fichiers de gouvernance sans accord ; pas de minuterie obligatoire ni d'interrogatoire permanent.

Pour une nouvelle conversation, joindre si possible `core/SKILL.md`, `core/references/commands.md` et `core/references/assessment.md`.

## Exemples

- `/learn Comprendre les invariants d'une HashMap avec Java`
- `/hint 2 Je ne comprends pas le resize`
- `/debug Mon test de suppression échoue après une collision`
- `/arch Quelle frontière entre Telegram et FastAPI dans Andandoo ?`
- `/retrieve Les concepts réellement étudiés au dernier lab`
- `/ship Ajoute les tests de validation d'un module en production`

Un `/ship` textuel ne donne pas automatiquement accès à un ordinateur ou un dépôt ; exécution selon outils et permissions disponibles.
