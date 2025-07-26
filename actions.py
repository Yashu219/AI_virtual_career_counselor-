from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionCareerSuggestion(Action):

    def name(self) -> Text:
        return "action_career_suggestion"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        education = tracker.get_slot("education")
        interest = tracker.get_slot("interest")

        if education and interest:
            education = education.lower().strip()
            interest = interest.lower().strip()

            user_input = tracker.latest_message.get("text", "").lower()

            # Normalize education
            if "puc" in education or "pre-university" in education:
                education = "puc"
            elif "10" in education:
                education = "10th"
            elif "ug" in education or "btech" in education or "degree" in education:
                education = "ug"
            elif "pg" in education or "mtech" in education or "msc" in education:
                education = "pg"

            response = "🤔 Based on your input, here are some suggestions:\n\n"

            # ✅ Case: Completed PUC
            if education == "puc" and any(word in user_input for word in ["completed", "finished", "done"]):
                if "coding" in interest or "computer" in interest or "pcmc" in interest:
                    response += (
                        "💻 You completed PCMC — great! Now you can pursue **BCA, BSc Computer Science, or Engineering in CSE/AI**. "
                        "You're on the right track for tech careers like software development, AI, and data science."
                    )
                elif "pcmb" in interest or "biology" in interest:
                    response += (
                        "🔬 Since you've completed PCMB, you can go for **MBBS, BDS, BSc**, or **Engineering** depending on your preference. "
                        "Think about whether you enjoy life sciences more or problem-solving through math/physics."
                    )
                else:
                    response += (
                        "🎓 Since you've finished PUC, consider degrees in **Commerce, Arts, or Science** based on your strengths. "
                        "Explore BCom, BBA, BA Psychology, or BSc programs — and see what clicks!"
                    )

            # ✅ Current school-level (PUC/10th)
            elif education in ["10th", "puc"]:
                if "science" in interest or "pcmb" in interest:
                    response += (
                        "🔬 You're at the school level and interested in science. You can choose **PCMB or PCMC** in PUC. "
                        "Later, explore **MBBS, Engineering, B.Sc (Physics/Chemistry/Biology)**, or even **Research & Teaching** roles."
                    )
                elif "coding" in interest or "computer" in interest or "pcmc" in interest:
                    response += (
                        "💻 You seem interested in tech! Opt for **PCMC in PUC**, then pursue **BCA, BSc CS, or BE in CSE/AI**. "
                        "You’ll have great scope in software and AI careers."
                    )
                else:
                    response += (
                        "📘 You can explore **PUC in Arts, Commerce, or Science** based on your interest. "
                        "Each opens paths to careers like CA, Design, Law, or Journalism."
                    )

            # ✅ UG level
            elif education == "ug":
                if "coding" in interest:
                    response += (
                        "👩‍💻 You're a UG student into coding. Aim for roles like **Software Developer, Data Analyst, or Web Developer**. "
                        "Practice DSA, do projects, contribute on GitHub, and apply for internships."
                    )
                elif "electronics" in interest:
                    response += (
                        "🔌 As an electronics student, explore **Embedded Systems, VLSI, IoT, or Robotics**. "
                        "Certifications and mini-projects will strengthen your profile."
                    )
                else:
                    response += (
                        "🌍 Based on your UG degree and interest, you can go for **MBA, Civil Services, Design, or Teaching**. "
                        "Take an interest test if you're unsure about your exact direction."
                    )

            # ✅ PG level
            elif education == "pg":
                response += (
                    "🎓 With PG qualifications, you can pursue **Research, Teaching, or high-level industry roles**. "
                    "Also explore certifications in **Cloud, Data Science, AI**, or prep for **GATE/NET/PhD**."
                )

            else:
                response = (
                    "📢 Please give valid education info like 10th, PUC, UG, PG and your interest."
                )

            dispatcher.utter_message(text=response)

        else:
            dispatcher.utter_message(
                text="🔍 I couldn't find both your education and interest. Please tell them again like 'PUC' and 'coding'."
            )

        return []
