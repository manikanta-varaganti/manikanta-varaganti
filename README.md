<div align="center">

<img src="assets/hero.svg" width="100%" alt="An editor window typing out about.py: a Python class describing Manikanta Varaganti, a software engineer" />

<br/>

<a href="https://www.linkedin.com/in/manikanta-varaganti"><img src="https://img.shields.io/badge/linkedin-%23565f89?style=flat-square&logo=linkedin&logoColor=7aa2f7&labelColor=1a1b26" alt="LinkedIn" /></a>
<a href="mailto:mkvaraganti@gmail.com"><img src="https://img.shields.io/badge/smtp-mkvaraganti%40gmail.com-%23565f89?style=flat-square&logo=gmail&logoColor=f7768e&labelColor=1a1b26" alt="Email" /></a>
<a href="https://manikanta-varaganti-resume.tiiny.site/"><img src="https://img.shields.io/badge/curl-resume-%23565f89?style=flat-square&logo=readme&logoColor=bb9af7&labelColor=1a1b26" alt="Resume" /></a>
<a href="https://m2i101.github.io"><img src="https://img.shields.io/badge/ssh-portfolio-%23565f89?style=flat-square&logo=githubpages&logoColor=9ece6a&labelColor=1a1b26" alt="Portfolio" /></a>
<img src="https://komarev.com/ghpvc/?username=manikanta-varaganti&label=GET+%2F&color=565f89&style=flat-square&labelColor=1a1b26" alt="Profile views" />

</div>

<img src="assets/divider.svg" width="100%" alt="" />

## `$ neofetch`

```text
  ┌──────────────┐       manikanta@github
  │ ░▒▓ MV ▓▒░   │       ──────────────────────────────────────
  │  { dev }     │       OS ........ Human 4.0 (uptime: 4 years)
  │  </ >        │       Shell ..... zsh
  └──────────────┘       Langs ..... Python · Go · TypeScript · SQL · Java
                         Infra ..... GCP · AWS · Kubernetes · Docker · Terraform
                         Data ...... PostgreSQL · Redis · Kafka · MongoDB
                         Focus ..... distributed systems · agent platforms · LLMs
                         Edu ....... M.S. Computer Science, UCF (GPA 4.0)
                         Kernel .... curiosity-5.1.0 (unbounded)
                         Mem ....... 16 tabs / ∞ ideas
                         Status .... compiling
```

<img src="assets/divider.svg" width="100%" alt="" />

## `main.py`

```python
from about import Engineer


class Manikanta(Engineer):
    def philosophy(self):
        yield "make it work"
        yield "make it right"
        yield "make it fast"
        yield "then ask: can it improve itself?"   # <- the fun part

    def reach_me(self):
        return "mkvaraganti@gmail.com"


if __name__ == "__main__":
    for step in Manikanta().philosophy():
        print(f"> {step}")
```

```console
$ python main.py
> make it work
> make it right
> make it fast
> then ask: can it improve itself?
```

<img src="assets/divider.svg" width="100%" alt="" />

## `complexity.py`

<div align="center">
  <img src="assets/complexity.svg" width="100%" alt="Animated Big-O chart: O(1), O(log n), O(n), O(n log n), O(n squared) and O(2^n) curves, with the exponential one labelled 'my curiosity'" />
</div>

<img src="assets/divider.svg" width="100%" alt="" />

## `git log --graph`

```console
$ git log --graph --decorate

● f7a9c21 (HEAD -> main, tag: commure)
│   Commure
│   Software Engineer  ·  Jun 2025 → Oct 2026
│
● d95b2a6 (tag: ucf)
│   University of Central Florida
│   Applied AI Research Engineer  ·  Sep 2023 → May 2025
│
● 83e1f7b (tag: deloitte)
    Deloitte
    Software Developer  ·  Jul 2021 → Jul 2023
```

<img src="assets/divider.svg" width="100%" alt="" />

## `skills.toml`

```toml
# last updated: from my resume, not from vibes

[languages]
core   = ["Python", "Go", "TypeScript", "JavaScript", "SQL"]
also   = ["Java", "Bash/Shell", "HTML/CSS"]

[backend]
frameworks   = ["FastAPI", "Node.js"]
apis         = ["REST", "GraphQL", "gRPC", "WebSockets"]
architecture = ["Microservices", "Event-Driven", "Temporal", "Apache Kafka", "Pub/Sub", "Cloud Tasks", "Feature Flags"]

[data]
relational = ["PostgreSQL", "MySQL"]
nosql      = ["MongoDB", "Redis"]
streaming  = ["Apache Kafka", "Apache Flink (CDC)"]

[cloud]
platforms = ["GCP", "AWS (EC2, S3, Lambda, DynamoDB)"]
delivery  = ["Kubernetes", "Docker", "Terraform", "Helm", "Argo CD"]

[observability]
metrics = ["Prometheus", "Grafana", "Datadog"]
logs    = ["ELK", "Splunk"]
traces  = ["OpenTelemetry"]

[ai.agents]
models  = ["Generative AI", "LLMs", "RAG", "Vector Databases", "vLLM on H100s"]
systems = ["Multi-Agent Systems", "Agent Orchestration", "Tool Calling", "MCP", "A2A", "Agent Skills"]
craft   = ["Context Engineering", "Loop Engineering", "Agent Harnesses"]
tooling = ["LangChain", "LangGraph", "Claude Code", "Gemini", "OpenAI Codex", "Cursor"]

[tools]
dev     = ["Git", "GitHub", "GitLab", "Postman", "Figma"]
testing = ["PyTest", "Playwright", "Selenium", "Jest"]
```

<div align="center">

**Languages & backend**

<img src="https://skillicons.dev/icons?i=python,go,ts,js,java,bash,html,css,nodejs,fastapi,graphql&perline=11&theme=dark" alt="Languages and backend" />

**Data, cloud & delivery**

<img src="https://skillicons.dev/icons?i=postgres,mysql,mongodb,redis,kafka,gcp,aws,kubernetes,docker,terraform&perline=10&theme=dark" alt="Data and cloud" />

**Observability & tools**

<img src="https://skillicons.dev/icons?i=prometheus,grafana,elasticsearch,react,git,github,gitlab,postman,selenium,figma&perline=10&theme=dark" alt="Observability and tools" />

**Distributed systems & delivery extras**

<img src="https://img.shields.io/badge/Temporal-292e42?style=flat-square&logo=temporal&logoColor=7dcfff&labelColor=1a1b26" alt="Temporal" />
<img src="https://img.shields.io/badge/Apache%20Flink-292e42?style=flat-square&logo=apacheflink&logoColor=7dcfff&labelColor=1a1b26" alt="Apache Flink" />
<img src="https://img.shields.io/badge/Helm-292e42?style=flat-square&logo=helm&logoColor=7dcfff&labelColor=1a1b26" alt="Helm" />
<img src="https://img.shields.io/badge/Argo%20CD-292e42?style=flat-square&logo=argo&logoColor=7dcfff&labelColor=1a1b26" alt="Argo CD" />
<img src="https://img.shields.io/badge/OpenTelemetry-292e42?style=flat-square&logo=opentelemetry&logoColor=7dcfff&labelColor=1a1b26" alt="OpenTelemetry" />
<img src="https://img.shields.io/badge/Datadog-292e42?style=flat-square&logo=datadog&logoColor=7dcfff&labelColor=1a1b26" alt="Datadog" />
<img src="https://img.shields.io/badge/Splunk-292e42?style=flat-square&logo=splunk&logoColor=7dcfff&labelColor=1a1b26" alt="Splunk" />
<img src="https://img.shields.io/badge/gRPC-292e42?style=flat-square&labelColor=1a1b26" alt="gRPC" />
<img src="https://img.shields.io/badge/Pub/Sub-292e42?style=flat-square&logo=googlecloud&logoColor=7dcfff&labelColor=1a1b26" alt="Pub/Sub" />
<img src="https://img.shields.io/badge/PyTest-292e42?style=flat-square&logo=pytest&logoColor=7dcfff&labelColor=1a1b26" alt="PyTest" />

**Agent systems & AI tooling**

<img src="https://img.shields.io/badge/LangChain-292e42?style=flat-square&logo=langchain&logoColor=bb9af7&labelColor=1a1b26" alt="LangChain" />
<img src="https://img.shields.io/badge/LangGraph-292e42?style=flat-square&logo=langchain&logoColor=bb9af7&labelColor=1a1b26" alt="LangGraph" />
<img src="https://img.shields.io/badge/MCP-292e42?style=flat-square&labelColor=1a1b26" alt="MCP" />
<img src="https://img.shields.io/badge/A2A-292e42?style=flat-square&labelColor=1a1b26" alt="A2A" />
<img src="https://img.shields.io/badge/RAG-292e42?style=flat-square&labelColor=1a1b26" alt="RAG" />
<img src="https://img.shields.io/badge/vLLM-292e42?style=flat-square&labelColor=1a1b26" alt="vLLM" />
<img src="https://img.shields.io/badge/Claude%20Code-292e42?style=flat-square&logo=claude&logoColor=bb9af7&labelColor=1a1b26" alt="Claude Code" />
<img src="https://img.shields.io/badge/Gemini-292e42?style=flat-square&logo=googlegemini&logoColor=bb9af7&labelColor=1a1b26" alt="Gemini" />
<img src="https://img.shields.io/badge/OpenAI%20Codex-292e42?style=flat-square&logo=openai&logoColor=bb9af7&labelColor=1a1b26" alt="OpenAI Codex" />
<img src="https://img.shields.io/badge/Cursor-292e42?style=flat-square&logo=cursor&logoColor=bb9af7&labelColor=1a1b26" alt="Cursor" />

</div>

<img src="assets/divider.svg" width="100%" alt="" />

## `ls -lah ~/projects`

```text
drwxr-xr-x  detection-of-motorcyclists-without-helmet/   # machines that see        [Jupyter]
drwxr-xr-x  branch-predictor/                            # machines that anticipate  [Python]
drwxr-xr-x  cache-simulator/                             # machines that remember    [Python]
drwxr-xr-x  internship-portal/                           # people, matched to chances [HTML]
drwxr-xr-x  Garbagemonitoring/                           # IoT meets the bin         [C++]
```

<div align="center">

<a href="https://github.com/manikanta-varaganti/detection-of-motorcyclists-without-helmet"><img width="48%" src="https://github-readme-stats.vercel.app/api/pin/?username=manikanta-varaganti&repo=detection-of-motorcyclists-without-helmet&theme=tokyonight&hide_border=false&border_color=292e42" alt="Helmet detection" /></a>
<a href="https://github.com/manikanta-varaganti/branch-predictor"><img width="48%" src="https://github-readme-stats.vercel.app/api/pin/?username=manikanta-varaganti&repo=branch-predictor&theme=tokyonight&hide_border=false&border_color=292e42" alt="Branch predictor" /></a>
<a href="https://github.com/manikanta-varaganti/cache-simulator"><img width="48%" src="https://github-readme-stats.vercel.app/api/pin/?username=manikanta-varaganti&repo=cache-simulator&theme=tokyonight&hide_border=false&border_color=292e42" alt="Cache simulator" /></a>
<a href="https://github.com/manikanta-varaganti/internship-portal"><img width="48%" src="https://github-readme-stats.vercel.app/api/pin/?username=manikanta-varaganti&repo=internship-portal&theme=tokyonight&hide_border=false&border_color=292e42" alt="Internship portal" /></a>

</div>

<img src="assets/divider.svg" width="100%" alt="" />

## `htop`

<div align="center">

<img height="170" src="https://github-readme-stats.vercel.app/api?username=manikanta-varaganti&show_icons=true&theme=tokyonight&hide_border=false&border_color=292e42&count_private=true&include_all_commits=true" alt="GitHub stats" />
<img height="170" src="https://github-readme-stats.vercel.app/api/top-langs/?username=manikanta-varaganti&layout=compact&langs_count=8&theme=tokyonight&hide_border=false&border_color=292e42" alt="Top languages" />

<img src="https://streak-stats.demolab.com/?user=manikanta-varaganti&theme=tokyonight&hide_border=false&border_radius=4.5" alt="GitHub streak" />

<img src="https://github-readme-activity-graph.vercel.app/graph?username=manikanta-varaganti&theme=tokyo-night&hide_border=true&area=true" alt="Contribution graph" width="100%" />

<img src="https://raw.githubusercontent.com/manikanta-varaganti/manikanta-varaganti/output/github-snake-dark.svg" alt="A snake eating my contribution graph" width="100%" />

</div>

<img src="assets/divider.svg" width="100%" alt="" />

## `TODO.md`

- [x] Ship systems that move 100,000+ files a month without dropping them
- [x] Serve LLMs on H100s and train across multi-node GPU clusters
- [x] Get 50+ engineers building agents without the boilerplate
- [x] Learn to read other people's code without sighing
- [ ] Build something that surprises its own author
- [ ] Understand what's actually going on inside the models
- [ ] Get to inbox zero (🙃)

<details>
<summary><code>sudo rm -rf /</code></summary>

<br/>

```console
$ sudo rm -rf /
rm: it is dangerous to operate recursively on '/'
rm: use --no-preserve-root to override this failsafe

nice try. 🙂  while you're here, my inbox is open: mkvaraganti@gmail.com
```

</details>

<img src="assets/divider.svg" width="100%" alt="" />

<div align="center">

```python
if __name__ == "__main__":
    coffee = True
    while coffee:
        build(); learn(); repeat()
```

<a href="https://www.linkedin.com/in/manikanta-varaganti"><img src="https://img.shields.io/badge/linkedin-%23565f89?style=flat-square&logo=linkedin&logoColor=7aa2f7&labelColor=1a1b26" alt="LinkedIn" /></a>
<a href="https://twitter.com/Manikanta_029"><img src="https://img.shields.io/badge/twitter-%23565f89?style=flat-square&logo=twitter&logoColor=7dcfff&labelColor=1a1b26" alt="Twitter" /></a>
<a href="https://www.instagram.com/manikantavaraganti"><img src="https://img.shields.io/badge/instagram-%23565f89?style=flat-square&logo=instagram&logoColor=f7768e&labelColor=1a1b26" alt="Instagram" /></a>
<a href="https://open.spotify.com/user/313crjkpqlch5ajaqsaglaevr6fa"><img src="https://img.shields.io/badge/spotify-%23565f89?style=flat-square&logo=spotify&logoColor=9ece6a&labelColor=1a1b26" alt="Spotify" /></a>

<br/><br/>

<a href="https://readme-jokes.vercel.app"><img src="https://readme-jokes.vercel.app/api?bgColor=%231a1b26&textColor=%23c0caf5&aColor=%237aa2f7&borderColor=%23292e42" alt="Random dev joke" /></a>

<sub><code>process exited with code 0</code></sub>

</div>
