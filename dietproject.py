import tkinter as tk
from tkinter import messagebox

def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    
    # BMI classification
    if bmi < 18.5:
        classification = "Underweight"
    elif 18.5 <= bmi <= 24.9:
        classification = "Normal weight"
    elif 25 <= bmi <= 29.9:
        classification = "Overweight"
    else:
        classification = "Obesity"                
        
    return bmi, classification

def generate_diet_plan(goal, diet_type):
    # Define the diet plans with recipes
    diet_plan = {
        "Day 1": {
            "Breakfast": ["Oatmeal", "Recipe: Cook oats with water or milk, add fruits or nuts.", "Alternative: Porridge with almond milk"],
            "Lunch": ["Salad with Chicken", "Recipe: Mixed greens, grilled chicken, olive oil, and lemon dressing.", "Alternative: Grilled tofu with salad"],
            "Dinner": ["Grilled Fish", "Recipe: Grill a fish fillet, add seasoning, and serve with steamed veggies.", "Alternative: Grilled mushrooms"]
        },
        "Day 2": {
            "Breakfast": ["Scrambled Eggs", "Recipe: Whisk eggs with a pinch of salt and pepper, cook in a pan.", "Alternative: Scrambled tofu"],
            "Lunch": ["Veggie Stir Fry", "Recipe: Stir fry vegetables like bell peppers, carrots, and broccoli.", "Alternative: Stir fry with egg and tofu"],
            "Dinner": ["Chicken Breast with Veggies", "Recipe: Grill chicken breast and serve with steamed veggies.", "Alternative: Grilled tempeh with veggies"]
        },
        "Day 3": {
            "Breakfast": ["Smoothie", "Recipe: Blend banana, spinach, almond milk, and protein powder.", "Alternative: Yogurt parfait with fruits and granola"],
            "Lunch": ["Quinoa Salad", "Recipe: Mix cooked quinoa with cucumbers, tomatoes, and a lemon dressing.", "Alternative: Brown rice salad with chickpeas"],
            "Dinner": ["Grilled Tofu or Chicken", "Recipe: Grill tofu or chicken breast and serve with a side of veggies.", "Alternative: Grilled tempeh or fish"]
        },
        "Day 4": {
            "Breakfast": ["Whole wheat toast with Avocado", "Recipe: Toast whole wheat bread and top with mashed avocado.", "Alternative: Toast with hummus"],
            "Lunch": ["Veggie Burger", "Recipe: Grill a veggie patty, serve with lettuce, tomato, and whole wheat bun.", "Alternative: Chicken burger or tempeh burger"],
            "Dinner": ["Roasted Salmon", "Recipe: Roast salmon with olive oil, garlic, and lemon.", "Alternative: Roasted portobello mushrooms"]
        },
        "Day 5": {
            "Breakfast": ["Yogurt with Fruits", "Recipe: Layer yogurt with fresh berries and granola.", "Alternative: Coconut yogurt with mixed nuts"],
            "Lunch": ["Veggie Wrap", "Recipe: Wrap hummus, cucumber, and avocado in a whole wheat tortilla.", "Alternative: Chicken wrap or tofu wrap"],
            "Dinner": ["Chicken Salad", "Recipe: Grilled chicken on a bed of greens with olive oil dressing.", "Alternative: Grilled tempeh or fish salad"]
        },
        "Day 6": {
            "Breakfast": ["Fruit Salad", "Recipe: Mix various fruits like apples, oranges, and berries.", "Alternative: Smoothie bowl with fruits and seeds"],
            "Lunch": ["Grilled Chicken with Veggies", "Recipe: Grill chicken and serve with steamed veggies.", "Alternative: Grilled tofu or tempeh"],
            "Dinner": ["Veggie Pasta", "Recipe: Boil whole wheat pasta and toss with veggies and olive oil.", "Alternative: Chicken or fish pasta"]
        },
        "Day 7": {
            "Breakfast": ["Oatmeal with Nuts", "Recipe: Cook oats and add chopped nuts and honey.", "Alternative: Porridge with chia seeds"],
            "Lunch": ["Lentil Soup", "Recipe: Boil lentils with garlic, onions, and veggies.", "Alternative: Chicken soup or tofu soup"],
            "Dinner": ["Baked Chicken with Veggies", "Recipe: Bake chicken with roasted vegetables.", "Alternative: Grilled tofu with roasted veggies"]
        }
    }

    # Modify diet plan according to the goal (weight loss, maintenance, or weight gain)
    if goal == "lose weight":
        # For weight loss, we may replace some meals with lower calorie options
        for day, meals in diet_plan.items():
            for meal, details in meals.items():
                details[0] = details[0] + " (Low Calorie)"
    
    # Modify meals according to the user's dietary preference
    if diet_type == "vegetarian":
        for day, meals in diet_plan.items():
            for meal, details in meals.items():
                details[0] = details[0].replace("Chicken", "Tofu").replace("Fish", "Grilled Tofu").replace("Salmon", "Tofu")
                details[2] = details[2].replace("Chicken", "Tofu").replace("Fish", "Grilled Tofu").replace("Salmon", "Tofu")
    
    elif diet_type == "eggitarian":
        for day, meals in diet_plan.items():
            for meal, details in meals.items():
                details[0] = details[0].replace("Chicken", "Egg").replace("Fish", "Egg").replace("Salmon", "Egg")
                details[2] = details[2].replace("Chicken", "Egg").replace("Fish", "Egg").replace("Salmon", "Egg")

    return diet_plan

def on_submit():
    # Get user input
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get())
        goal = goal_var.get()
        diet_type = diet_type_var.get()
        
        # Calculate BMI and classification
        bmi, classification = calculate_bmi(weight, height)
        bmi_label.config(text=f"Your BMI: {bmi:.2f} - {classification}")
        
        # Display motivational quote if needed
        if goal == "lose weight":
            motivation_label.config(text="Motivational Quote: 'The harder you work for something, the greater you'll feel when you achieve it.'")
        elif goal == "gain weight":
            motivation_label.config(text="Motivational Quote: 'Success is the sum of small efforts, repeated day in and day out.'")
        else:
            motivation_label.config(text="")
        
        # Display perfect weight message
        if classification == "Normal weight":
            messagebox.showinfo("Perfect Weight", "Your weight is perfect! Keep it up!")
        
        # Generate diet plan
        diet_plan = generate_diet_plan(goal, diet_type)
        
        # Display diet plan
        diet_plan_text = "Your Diet Plan for the Week:\n\n"
        for day, meals in diet_plan.items():
            diet_plan_text += f"{day}:\n"
            for meal, details in meals.items():
                diet_plan_text += f"  {meal}: {details[0]}\n"
                diet_plan_text += f"    Alternative: {details[2]}\n"
        
        if recipe_var.get() == 1:
            diet_plan_text += "\nRecipes for Meals:\n"
            for day, meals in diet_plan.items():
                diet_plan_text += f"{day}:\n"
                for meal, details in meals.items():
                    diet_plan_text += f"  {meal}: {details[1]}\n"

        # Clear the existing content and add new content to output area
        output_text.config(state=tk.NORMAL)  # Enable editing the text widget
        output_text.delete(1.0, tk.END)  # Clear any previous content
        output_text.insert(tk.END, diet_plan_text)  # Insert the new diet plan text
        output_text.config(state=tk.DISABLED)  # Disable editing to make it read-only

        # Estimate days to reach goal
        if goal == "lose weight":
            goal_weight = float(goal_weight_entry.get())
            days_needed = (weight - goal_weight) * 7
            goal_duration_label.config(text=f"Estimated time to reach goal: {days_needed:.0f} days")
        
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numerical values for weight and height")

def on_goal_weight_submit():
    global goal_weight_entry
    goal_weight = float(goal_weight_entry.get())
    goal_duration_label.config(text=f"Goal Weight: {goal_weight}")

# Set up the GUI window
root = tk.Tk()
root.title("BMI and Diet Plan Calculator")

# Weight and Height Input
weight_label = tk.Label(root, text="Enter your weight (kg):")
weight_label.pack()
weight_entry = tk.Entry(root)
weight_entry.pack()

height_label = tk.Label(root, text="Enter your height (m):")
height_label.pack()
height_entry = tk.Entry(root)
height_entry.pack()

# Goal input
goal_label = tk.Label(root, text="What is your goal? (lose weight, gain weight, maintain weight):")
goal_label.pack()
goal_var = tk.StringVar()
goal_var.set("maintain weight")
goal_menu = tk.OptionMenu(root, goal_var, "lose weight", "gain weight", "maintain weight")
goal_menu.pack()

# Diet Type input (Vegetarian, Eggitarian, Non-Vegetarian)
diet_type_label = tk.Label(root, text="Select your diet type:")
diet_type_label.pack()
diet_type_var = tk.StringVar()
diet_type_var.set("non-vegetarian")
diet_type_menu = tk.OptionMenu(root, diet_type_var, "vegetarian", "eggitarian", "non-vegetarian")
diet_type_menu.pack()

# Goal Weight
goal_weight_label = tk.Label(root, text="Enter your goal weight (kg):")
goal_weight_label.pack()
goal_weight_entry = tk.Entry(root)
goal_weight_entry.pack()

goal_weight_button = tk.Button(root, text="Submit Goal Weight", command=on_goal_weight_submit)
goal_weight_button.pack()

# Ask for Recipe
recipe_var = tk.IntVar()
recipe_check = tk.Checkbutton(root, text="Do you want the recipes for each meal?", variable=recipe_var)
recipe_check.pack()

# Submit Button
submit_button = tk.Button(root, text="Submit", command=on_submit)
submit_button.pack()

# Labels for output
bmi_label = tk.Label(root, text="Your BMI: ")
bmi_label.pack()

motivation_label = tk.Label(root, text="")
motivation_label.pack()

goal_duration_label = tk.Label(root, text="Goal Duration: ")
goal_duration_label.pack()

# Create a scrollable frame for the output text
output_text = tk.Text(root, height=15, width=80, wrap=tk.WORD)
output_text.pack(padx=10, pady=10)

# Disable editing the text widget by default
output_text.config(state=tk.DISABLED)

# Run the GUI
root.mainloop()
