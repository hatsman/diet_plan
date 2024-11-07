class User:
    def __init__(self, name, age, weight, height, gender, goals, activity_level):
        self.name = name
        self.age = age
        self.weight = weight
        self.height = height
        self.gender = gender
        self.goals = goals
        self.activity_level = activity_level

    def calculate_bmr(self):
        if self.gender == 'male':
            bmr = (10 * self.weight) + (6.25 * self.height) - (5 * self.age) + 5
        elif self.gender == 'female':
            bmr = (10 * self.weight) + (6.25 * self.height) - (5 * self.age) - 161
        return bmr

    def calculate_daily_caloric_needs(self):
        bmr = self.calculate_bmr()

        # Map activity level to the corresponding factor
        activity_factors = {
            'sedentary': 1.2,
            'lightly_active': 1.375,
            'moderately_active': 1.55,
            'very_active': 1.725,
            'extra_active': 1.9
        }

        # Calculate daily caloric needs based on activity level
        daily_caloric_needs = bmr * activity_factors.get(self.activity_level, 1)

        # Adjust based on goals
        if self.goals == 'lose_fat':
            daily_caloric_needs *= 0.8
        elif self.goals == 'build_muscle':
            daily_caloric_needs *= 1.2
        elif self.goals == 'maintain_weight':
            daily_caloric_needs *= 1

        return daily_caloric_needs

    def calculate_macronutrient_requirements(self):
        daily_caloric_needs = self.calculate_daily_caloric_needs()

        # Calculate macronutrient breakdown
        protein = 1.6 * self.weight  # 1.6g protein per kg of body weight
        carbohydrates = (daily_caloric_needs * 0.55) / 4  # 55% of calories from carbs, 1g carbs = 4 kcal
        fat = (daily_caloric_needs * 0.25) / 9  # 25% of calories from fat, 1g fat = 9 kcal

        return {
            'protein': protein,
            'carbohydrates': carbohydrates,
            'fat': fat
        }
