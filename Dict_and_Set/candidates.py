required_skills = ("Python", "github", "linux")

candidates = {
    "anna": {"java", "linux", "windows", "github", "Python", "Fullstack"},
    "Bob": {"github", "linux", "Python"},
    "carol": {"linux", "javascipt", "Html", "Python", "github"},
    "daniel": {"pascal", "java", "c++", "github"},
    "ekani": {"Html", "github", "Python", "linux", "css"},
    "fenna": {"linux", "pascal", "java", "c", "lisp", "modula-2", "perl", "github"},
}
intervieews = set()
for candidate, skills in candidates.items():
    # if skills.issuperset(required_skills):
    if skills > set(required_skills):
        intervieews.add(candidate)

print(intervieews)
