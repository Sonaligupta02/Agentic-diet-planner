# 🍽️ Agentic Diet Planner

A Python-based intelligent meal planning application that leverages AI agents to create personalized, nutritionally-balanced diet plans based on individual preferences, dietary restrictions, and health goals.

## ✨ Features

- **AI-Powered Meal Planning**: Intelligent agents generate personalized meal plans tailored to your dietary needs
- **Nutritional Analysis**: Detailed nutritional information for every meal suggestion
- **Flexible Preferences**: Support for various dietary restrictions (vegan, gluten-free, keto, etc.)
- **Health Goal Tracking**: Create plans aligned with your wellness objectives (weight loss, muscle gain, maintenance)
- **Recipe Recommendations**: Curated recipe suggestions with ingredients and cooking instructions
- **User-Friendly Interface**: Intuitive interaction with the planning system

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- pip (Python package installer)

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Sonaligupta02/Agentic-diet-planner.git
   cd Agentic-diet-planner
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

### Usage

```python
from diet_planner import DietPlanner

# Initialize the planner
planner = DietPlanner()

# Generate a meal plan
meal_plan = planner.create_plan(
    dietary_preference="vegetarian",
    health_goal="weight_loss",
    duration_days=7
)

print(meal_plan)
```

## 📁 Project Structure

```
Agentic-diet-planner/
├── README.md
├── requirements.txt
├── agent.py
├── app.py
├── tools.py
```

## 🔧 Configuration

Create a `.env` file in the project root for configuration:

```env
# API Keys (if applicable)
API_KEY=your_api_key_here

```

## 📚 Documentation

For detailed documentation and advanced usage, please refer to:
- [Getting Started Guide](docs/getting-started.md)
- [API Reference](docs/api-reference.md)
- [Configuration Guide](docs/configuration.md)


## 📧 Contact

For questions or inquiries, feel free to reach out:
- **GitHub**: [@Sonaligupta02](https://github.com/Sonaligupta02)
- **Issues**: [GitHub Issues](https://github.com/Sonaligupta02/Agentic-diet-planner/issues)

---

**Happy Planning! 🌟**
