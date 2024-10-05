import tkinter as tk
from tkinter import messagebox
import random

class AnimalKingdomTrivia:
    def __init__(self, master):
        self.master = master
        self.master.title("Animal Kingdom Trivia")
        self.master.geometry("600x400")
        self.master.resizable(False, False)

        self.questions = [
            {
                "question": "Which animal has the longest lifespan?",
                "options": ["Elephant", "Tortoise", "Bowhead Whale", "Greenland Shark"],
                "answer": "Greenland Shark",
                "fact": "Greenland Sharks can live for up to 500 years, making them the longest-living vertebrate known!"
            },
            {
                "question": "Which animal has the highest blood pressure?",
                "options": ["Giraffe", "Elephant", "Hummingbird", "Blue Whale"],
                "answer": "Giraffe",
                "fact": "Giraffes have extremely high blood pressure (up to 300/180 mmHg) to pump blood all the way up their long necks to their brains."
            },
            {
                "question": "Which animal never sleeps?",
                "options": ["Dolphin", "Bullfrog", "Bat", "Koala"],
                "answer": "Bullfrog",
                "fact": "Bullfrogs never sleep. They rest with their eyes open, always alert for predators."
            },
            {
                "question": "Which animal has the most powerful bite?",
                "options": ["Hippopotamus", "Crocodile", "Great White Shark", "Jaguar"],
                "answer": "Crocodile",
                "fact": "The saltwater crocodile has the strongest bite of any animal, with a bite force of up to 3,700 pounds per square inch!"
            },
            {
                "question": "Which animal has the longest migration?",
                "options": ["Monarch Butterfly", "Humpback Whale", "Arctic Tern", "Leatherback Turtle"],
                "answer": "Arctic Tern",
                "fact": "The Arctic Tern migrates from the Arctic to the Antarctic and back again each year, covering up to 44,000 miles!"
            },
            {
                "question": "Which animal has the largest eyes?",
                "options": ["Giant Squid", "Elephant", "Ostrich", "Tarsier"],
                "answer": "Giant Squid",
                "fact": "The giant squid has the largest eyes in the animal kingdom, measuring up to 10 inches in diameter!"
            },
            {
                "question": "Which animal can regenerate its brain?",
                "options": ["Starfish", "Planarian Worm", "Axolotl", "Sea Cucumber"],
                "answer": "Planarian Worm",
                "fact": "Planarian worms can regenerate their entire bodies, including their brains, from just a small piece of tissue."
            },
            {
                "question": "Which animal has the best sense of smell?",
                "options": ["Elephant", "Bloodhound", "Bear", "Shark"],
                "answer": "Bear",
                "fact": "The bear's sense of smell is 7 times better than a bloodhound's and 2,100 times better than a human's."
            },
            {
                "question": "Which animal can survive without a head for weeks?",
                "options": ["Cockroach", "Praying Mantis", "Flatworm", "Starfish"],
                "answer": "Cockroach",
                "fact": "Cockroaches can survive for weeks without their heads, only dying from the inability to eat."
            },
            {
                "question": "Which animal has the longest gestation period?",
                "options": ["Elephant", "Blue Whale", "Giraffe", "Frilled Shark"],
                "answer": "Frilled Shark",
                "fact": "The frilled shark has the longest gestation period of any animal, lasting up to 3.5 years!"
            },
            {
                "question": "Which animal can clone itself?",
                "options": ["Jellyfish", "Starfish", "Komodo Dragon", "All of the above"],
                "answer": "All of the above",
                "fact": "Jellyfish, starfish, and Komodo dragons can all reproduce asexually through various forms of cloning."
            },
            {
                "question": "Which animal has the most toxic venom?",
                "options": ["Box Jellyfish", "Inland Taipan", "Blue-ringed Octopus", "Stonefish"],
                "answer": "Box Jellyfish",
                "fact": "The box jellyfish is considered the most venomous marine animal, with venom capable of killing a human in minutes."
            },
            {
                "question": "Which animal can survive being frozen?",
                "options": ["Wood Frog", "Arctic Fox", "Polar Bear", "Penguin"],
                "answer": "Wood Frog",
                "fact": "The wood frog can survive being frozen solid, with its heart stopping and ice crystals forming in its blood."
            },
            {
                "question": "Which animal has the highest body temperature?",
                "options": ["Hummingbird", "Desert Ant", "Pompeii Worm", "Human"],
                "answer": "Pompeii Worm",
                "fact": "The Pompeii worm can withstand temperatures up to 176°F (80°C), the highest of any animal on Earth."
            },
            {
                "question": "Which animal has the longest lifespan in captivity?",
                "options": ["Giant Tortoise", "Koi Fish", "Macaw", "Lake Sturgeon"],
                "answer": "Koi Fish",
                "fact": "The longest-living koi fish, Hanako, lived to be 226 years old, verified by scientific analysis of its scales."
            },
            {
                "question": "Which animal has the best memory?",
                "options": ["Elephant", "Dolphin", "Chimpanzee", "Pigeon"],
                "answer": "Dolphin",
                "fact": "Dolphins can remember whistles of other dolphins after 20 years of separation, showing the longest-lasting memory in the animal kingdom."
            },
            {
                "question": "Which animal can change its sex?",
                "options": ["Clownfish", "Wrasse", "Parrotfish", "All of the above"],
                "answer": "All of the above",
                "fact": "Clownfish, wrasses, and parrotfish can all change their sex in response to environmental or social cues."
            },
            {
                "question": "Which animal has the most hearts?",
                "options": ["Octopus", "Earthworm", "Hagfish", "Cockroach"],
                "answer": "Hagfish",
                "fact": "The hagfish has four hearts - one main heart and three accessory pumps that help circulate its blood."
            },
            {
                "question": "Which animal can survive the longest without water?",
                "options": ["Kangaroo Rat", "Camel", "Gila Monster", "Tortoise"],
                "answer": "Kangaroo Rat",
                "fact": "The kangaroo rat can survive its entire life without drinking water, getting all the moisture it needs from the seeds it eats."
            },
            {
                "question": "Which animal has the fastest acceleration?",
                "options": ["Cheetah", "Peregrine Falcon", "Mantis Shrimp", "Flea"],
                "answer": "Mantis Shrimp",
                "fact": "The mantis shrimp's strike is so fast it boils the water around it, creating a shockwave that can kill prey even if the shrimp misses."
            }
        ]
        
        self.score = 0
        self.current_question = 0
        
        self.question_label = tk.Label(master, text="", wraplength=500, font=("Arial", 14))
        self.question_label.pack(pady=20)
        
        self.var = tk.StringVar()
        self.option_buttons = []
        for i in range(4):
            button = tk.Radiobutton(master, text="", variable=self.var, value="", font=("Arial", 12))
            button.pack(pady=5)
            self.option_buttons.append(button)
        
        self.submit_button = tk.Button(master, text="Submit", command=self.check_answer)
        self.submit_button.pack(pady=20)
        
        self.score_label = tk.Label(master, text="Score: 0", font=("Arial", 12))
        self.score_label.pack(pady=10)
        
        random.shuffle(self.questions)
        self.load_question()
    
    def load_question(self):
        if self.current_question < len(self.questions):
            question = self.questions[self.current_question]
            self.question_label.config(text=question["question"])
            options = question["options"]
            random.shuffle(options)
            for i, option in enumerate(options):
                self.option_buttons[i].config(text=option, value=option)
            self.var.set(None)
        else:
            self.show_final_score()
    
    def check_answer(self):
        if not self.var.get():
            messagebox.showwarning("Warning", "Please select an answer!")
            return
        
        question = self.questions[self.current_question]
        if self.var.get() == question["answer"]:
            self.score += 1
            result = "Correct!"
        else:
            result = f"Wrong! The correct answer is {question['answer']}."
        
        self.score_label.config(text=f"Score: {self.score}")
        messagebox.showinfo("Result", f"{result}\n\nFun Fact: {question['fact']}")
        
        self.current_question += 1
        self.load_question()
    
    def show_final_score(self):
        messagebox.showinfo("Game Over", f"Final Score: {self.score}/{len(self.questions)}")
        if messagebox.askyesno("Play Again?", "Do you want to play again?"):
            self.reset_game()
        else:
            self.master.quit()
    
    def reset_game(self):
        self.score = 0
        self.current_question = 0
        self.score_label.config(text="Score: 0")
        random.shuffle(self.questions)
        self.load_question()

root = tk.Tk()
game = AnimalKingdomTrivia(root)
root.mainloop()
