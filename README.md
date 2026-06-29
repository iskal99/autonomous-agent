# 🤖 Agent IA Autonome

Un agent IA puissant et autonome qui gère des tâches de développement de manière indépendante.

## ✨ Fonctionnalités

- 🧠 **Intelligence autonome** : Analyse les tâches et les exécute sans intervention
- 🔄 **Auto-correction** : Détecte les erreurs et les corrige automatiquement
- 📋 **Planification intelligente** : Décompose les tâches complexes en sous-tâches
- 🧪 **Tests intégrés** : Vérifie le code généré
- 📝 **Documentation auto** : Génère automatiquement la documentation
- 🔗 **GitHub intégré** : Crée branches, commits, PR automatiquement
- 📊 **Rapports détaillés** : Trace toutes les actions effectuées

## 🚀 Démarrage rapide

### Installation locale

```bash
git clone https://github.com/iskal99/autonomous-agent.git
cd autonomous-agent
pip install -r requirements.txt
```

### Utilisation

**Via CLI local :**
```bash
python agent.py --task "Créer une API REST en Python"
```

**Via GitHub Actions :**
- Créer une issue avec le label `agent-task`
- L'agent exécute automatiquement

**Via workflow manual :**
```bash
gh workflow run agent-autonome.yml -f task="Votre tâche"
```

## 📁 Structure du projet

```
autonomous-agent/
├── .github/workflows/
│   ├── agent-autonome.yml          # Workflow principal
│   └── agent-test.yml              # Tests de l'agent
├── agent/
│   ├── __init__.py
│   ├── core.py                     # Cœur de l'agent
│   ├── config.py                   # Configuration
│   ├── logger.py                   # Logging
│   └── tools/
│       ├── __init__.py
│       ├── git_ops.py              # Opérations Git
│       ├── code_generator.py       # Génération de code
│       ├── test_runner.py          # Exécution de tests
│       └── github_api.py           # Intégration GitHub
├── tests/
│   └── test_agent.py               # Tests unitaires
├── config.json                     # Configuration globale
├── requirements.txt                # Dépendances Python
└── README.md                       # Ce fichier
```

## 🎯 Capacités de l'agent

### 1. Analyse des tâches
- Détecte le type de tâche (feature, bugfix, test, docs, refactor)
- Décompose en sous-tâches managérables
- Évalue la complexité

### 2. Planification
- Crée un plan d'exécution
- Gère les dépendances entre tâches
- Optimise l'ordre d'exécution

### 3. Exécution
- Crée automatiquement une branche Git
- Génère le code selon les specs
- Écrit les tests
- Exécute les tests
- Crée les commits

### 4. Vérification
- Valide le code généré
- Exécute les tests
- Vérifie la couverture de code
- Vérifie le respect des standards

### 5. Correction automatique
- Détecte les erreurs
- Analyse les causes
- Corrige et retry
- Boucle jusqu'à succès

### 6. Reporting
- Génère des rapports détaillés
- Documente les changements
- Crée la PR avec description
- Notifie les développeurs

## 📊 Exemple d'exécution

```
🚀 Agent Autonome démarré
📋 Analyse de la tâche: "Ajouter authentification JWT"
✅ Type détecté: feature
✅ Sous-tâches: 6
  1. Créer une branche
  2. Analyser les requirements
  3. Implémenter le code
  4. Écrire les tests
  5. Lancer les tests
  6. Créer la PR

🌿 Branche créée: agent/auth-jwt-1234567
🔨 Implémentation en cours...
✅ Code généré: src/auth/jwt.py
🧪 Tests en cours...
✅ 12/12 tests passants
📤 PR créée: #42
✅ Agent Autonome terminé
```

## 🔧 Configuration

Modifiez `config.json` pour personnaliser le comportement :

```json
{
  "agent": {
    "name": "DevAgent",
    "description": "Agent autonome pour développement",
    "autonomy_level": "advanced"
  },
  "execution": {
    "auto_create_branches": true,
    "auto_commit": true,
    "auto_create_pr": true,
    "require_tests": true,
    "max_retries": 3
  },
  "tools": {
    "git": true,
    "github": true,
    "python": true,
    "nodejs": true
  }
}
```

## 🔐 Variables d'environnement

Définissez les variables pour l'authentification GitHub :

```bash
export GITHUB_TOKEN=ghp_xxxxx
export GITHUB_REPOSITORY=iskal99/autonomous-agent
```

## 📚 Documentation

- [Guide complet](./docs/GUIDE.md)
- [API de l'agent](./docs/API.md)
- [Exemples d'utilisation](./docs/EXAMPLES.md)
- [Troubleshooting](./docs/TROUBLESHOOTING.md)

## 🐛 Troubleshooting

### L'agent ne démarre pas
```bash
# Vérifier les logs
python agent.py --debug

# Vérifier la configuration
python agent.py --config
```

### Les tests échouent
```bash
# Exécuter les tests localement
pytest tests/ -v

# Voir les logs détaillés
python agent.py --verbose
```

## 🤝 Contribution

Les contributions sont bienvenues ! Consultez [CONTRIBUTING.md](./CONTRIBUTING.md)

## 📄 License

MIT - Voir [LICENSE](./LICENSE)

## 👤 Auteur

Créé par **iskal99** avec ❤️

---

## 🎯 Prochaines étapes

1. ✅ Cloner le repo
2. ✅ Installer les dépendances
3. ✅ Configurer les variables d'environnement
4. ✅ Lancer l'agent : `python agent.py --task "Votre tâche"`

**Besoin d'aide ?** → Ouvrez une issue ! 🙋

