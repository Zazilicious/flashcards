import tkinter as tk

# Flashcards 
flashcards = [
    # Chapter 1
    ("Counseling", "A professional relationship that empowers diverse individuals, families, and groups in mental health, wellness, education, career."),
    ("Compassion fatigue", "Apathy to those who are suffering due to overexposure to people in need."),
    ("Burnout", "1) Emotional and physical exhaustion 2) Cynicism 3) Decreased perceived efficacy"),
    ("Levels of helping", "1) Non-professional (informal) 2) Generalist human services workers 3) Professional helpers (therapists etc.)"),
    ("NBCC", "National Board of Certified Counselors; awards the National Certified Counselor (NCC)."),
    ("CACREP", "Council for Accreditation of Counseling and Related Educational Programs"),
    ("Attribution", "What the counselor attributes the cause of a client’s problem to"),
    ("System", "A unified and organized set of ideas, principles, and behaviors."),
    ("Medical model", "Client not responsible; counselor is expert."),
    ("Moral model", "Clients are responsible for causing and solving problems; counselor is coach."),
    ("Compensatory model", "Clients are responsible for solving but not causing problems; counselor is teacher."),
    ("Enlightenment model", "Clients are responsible for causing problems but not solving them; counselor is authority figure."),
    
    
    # Chapter 2
    ("Ethics", "Philosophical discipline concerned with human conduct and moral decision making."),
    ("Professional Ethics", "Beliefs about behavior and conduct that guide professional practices."),
    ("Morality", "Judgment or evaluation of an action as right, wrong, good, bad, ought, should."),
    ("Law", "The precise codification of governing standards established to ensure legal and moral justice."),
    ("Unethical behaviors", "Violating confidentiality, exceeding competency, negligent practice, false expertise, imposing values, dependency, sex with client, dual relationships, financial issues, improper advertising, plagiarism."),
    ("ethics values in counseling", "ASERVIC (Association for Spiritual, Ethical, and Religious values in Counselin)"),
    ("ACA Ethics headings", "A) Counseling relationship B) Confidentiality C) Professional Responsibility D) Relationships with Others E) Evaluation F) Supervision G) Research H) Resolving Ethical Issues"),
    ("Six ethical principles", "Beneficence, Nonmaleficence, Autonomy, Justice, Fidelity, Veracity"),
    ("Five-stage developmental continuum", "1) Punishment 2) Institutional 3) Societal 4) Individual 5) Principle"),
    ("How to judge actions to take:", "Publicity, justice, moral traces (feelings of doubt), universality"),
    ("Tarasoff V. Board of Regents of the University of California (1976", "-guy in therapy said he was gonna kill his girlfriend, psychologist notified police, police did nothing, guy killed his girlfriend, parents of Tatiana Tarasoff sue the university for failing to notify the victim of a threat against her, California Supreme Court ruled in parents favor, therapists have the duty to protect the public that overrides any obligation to maintain client confidentiality."),
    ("Bogust V. Iverson (1960)","Counselor with a doctoral degree cannot be held liable for the suicide of one of his clients because counselors were merely teachers."),
    ("Iowa Law Review Note (1971)", "Counselors legally recognized as professionals who provided personal as well as vocational and educational counseling"),
    ("Weldon v. Virginia State Board of Psychologists Examiners", "Counseling is a professional distinct from psychology"),
    ("Liability", "have counselors caused harm to clients"),
    ("Malpractice", "harm to client caused by negligence"),
    ("Negligence", "departure from acceptable professional standards"),
    ("3 ways to protect oneself from malpractice)", "a) follow professional codes of ethics, b) follow normal practice standards, c) act professionally, attentively, and courteously."),
    ("Liability", "legal responsibility for something"),
    
    
    # Chapter 3
    ("Self-awareness", "Developing self-awareness from the inside out."),
    ("Awareness of others", "Developing awareness of others from the outside in."),
    
    # Chapter 4
    ("ADAA", "Association for Adult Development and Aging"),
    ("Development", "Systematic change that is lifelong and cumulative."),
    ("Young-Old", "65-75 years"),
    ("Old", "75+ years"),
    ("Old-Old", "85+ years"),
    ("Ageism", "Age-based expectations and prejudices"),
    ("Sexism", "Belief that females should be treated based on sex, ignoring other criteria"),
    ("Pink-color jobs", "Jobs that primarily employ women"),
    ("Feminist theory", "Focuses on female development as persons with common and unique qualities"),
    ("ALGBTIC", "Association for Lesbian, Gay, Bisexual, and Transgender Issues in Counseling (ALGBTIC)"),
    ("SEM", "Social Empowerment Model: increases collective and personal self-advocacy for LGBTQ+"),
    ("GRC", "Gender Role Conflict: empowers trans people to live life on their own terms"),
    ("ADDRESSING Model", "A- age, D- developmental disabilities, D- acquired disabilities, R- religion, E- ethnicity, S- social status, S- sexual orientation, I- indigenous heritage, N- national origin, G- gender"),
    
    # Chapter 5
    ("Battle for structure", "Issues of administrative control (scheduling, fees, etc.)"),
    ("Battle for initiative", "Motivation for change and client responsibility"),
    ("Microskills", "Counselor responses that cut across cultural and theoretical lines"),
    ("Structure", "Practical guidelines (time limits, action limits, role limits, and procedural limits), Professional disclosure statements (include details about the nature of counseling, expectations, responsibilities, methods, and ethics of counseling)"),
    ("Initiative", "Motivation to change"),
    ("Problems of initiative", "Reluctant client, Resistant Client"),
    ("Direct persuasion techniques", "Foot-in-the-door, Door-in-the-face"),
    ("Confrontation", "the counselor points out to the client what the client is doing, i.e.inconsistencies."),
    ("Metaphors", "can be used to teach and reduce threat levels"),
    ("mattering", "the belief that as humans we are important and significant to the world around us and the lives of others"),
    ("Eight common characteristics of space and their potential impact", "Accessories, Color, Furniture and room design, Lighting, Smell, Sound, Texture, Thermal conditions"),
    ("Proxemics", "the distance between counselor and client; Average range of comfort is between 30-39 inches, with chairs set at a 90 degree angle"),
    ("YAVIS", "Young, Attractive, Verbal, Intelligent, Successful clients (more successful)"),
    ("HOUNDs", "Homely, Old, Unintelligent, Nonverbal, Disadvantaged clients (less successful)"),
    ("Informed-oriented first interview", "Includes probes, closed questions, requests for clarification"),
    ("Relationship-oriented fist interview", "Includes restatement, reflection of feelings, summary of feelings, and acknowledgement of nonverbal behavior"),
    ("Rapport", "genuine interest in and accepting of the client"),
    ("Two important micro skills for rapport building are:", "-Attending behavior, -client-observation skills"),
    ("Attentiveness", "the amount of verbal and nonverbal behavior shown to the client"),
    ("5 nonverbal skills involve initial attending, known as SOLER:", "Face the client Squarely, Adopt an Open posture, -Lean toward the client, -Appropriate Eye contact,Relax and be comfortable "),
    ("Four major actions that usually block the counselor-client communication and should be generally avoided:", "-Advice-giving,-Lecturing, -Excessive questioning,  -Storytelling by the counselor"),
    ("Unfocused goals", " not identified, too broad, or not prioritized"),
    ("Unrealistic goals", "may include happiness, perfection, progress, being number one, and self-actualization. They have merit but are not easily obtained or sustained."),
    ("Uncoordinated goals", "all into either really uncoordinated (incompatibility between goals and client) or seemingly uncoordinated (appear to be uncoordinated but really are not)"),
    ("Dryer and Vriend (1977) 7 specific criteria for", "MSRAQBBU: Mutually Agreed on , Specific, Relevant to self-defeating behavior, achievement oriented, quantifiable and measurable, behavioral and observable, understandable and cab be restated clearly"),
    ("Empathy", "Counselor’s ability to enter the client’s world without losing 'as if' quality"),
    ("SBIRT", "Screening, Brief Intervention, Referral to Treatment model for substance use disorders"),
]

current_index = 0
showing_answer = False  # Tracks whether definition is showing

# GUI Functions
def flip_card():
    global showing_answer
    showing_answer = not showing_answer
    animate_flip(show_answer=showing_answer)
    flip_button.config(text="Flip")

def next_card():
    global current_index, showing_answer
    current_index += 1
    if current_index >= len(flashcards):
        current_index = 0
    showing_answer = False
    animate_flip(next_card=True)
    flip_button.config(text="Flip")

def animate_flip(show_answer=False, next_card=False):
    steps = 10
    shrink_width = card_frame.winfo_width()
    
    def shrink(step):
        if step > 0:
            card_frame.config(width=int(shrink_width * step / steps))
            root.after(20, shrink, step-1)
        else:
            if next_card:
                card_text.set(flashcards[current_index][0])
            elif show_answer:
                card_text.set(flashcards[current_index][1])
            else:
                card_text.set(flashcards[current_index][0])
            expand(1)
    
    def expand(step):
        if step <= steps:
            card_frame.config(width=int(shrink_width * step / steps))
            root.after(20, expand, step+1)
    
    shrink(steps)

# GUI setup
root = tk.Tk()
root.title("Flashcards - Principles of Philosophy")
root.geometry("650x400")
root.config(bg="#f0f0f0")

card_text = tk.StringVar()
card_text.set(flashcards[current_index][0])

card_frame = tk.Frame(root, bg="white", bd=2, relief="raised", width=500, height=250)
card_frame.pack(pady=50)
card_label = tk.Label(card_frame, textvariable=card_text, wraplength=450, font=("Arial", 16), bg="white")
card_label.place(relx=0.5, rely=0.5, anchor="center")

# Buttons frame side by side
button_frame = tk.Frame(root, bg="#f0f0f0")
button_frame.pack(pady=10)

flip_button = tk.Button(button_frame, text="Flip", command=flip_card, width=15, height=2, bg="#4CAF50", fg="white", font=("Arial", 12))
flip_button.pack(side="left", padx=10)

next_button = tk.Button(button_frame, text="Next Card", command=next_card, width=15, height=2, bg="#2196F3", fg="white", font=("Arial", 12))
next_button.pack(side="left", padx=10)

root.mainloop()
