header_block = """                <h1 class="text-center mb-1"><strong>{name}</strong></h1>
                <h4 class="text-center mt-1 mb-1">{expertise}</h4>
                <h6 class="text-center">{content}</h6>"""

summary_block = """                <div class="row">
                    <div class="title-line-wrapper text-center">
                        <span class="title-line-before"></span>
                        <h4 class="titles"><strong>Professional Summary</strong></h4>
                        <span class="title-line-after"></span>
                    </div>
                </div>
                <p class="text-justify mb-1">{summary}</p>"""

skills_heading = """                <div class="row mb-1">
                    <div class="title-line-wrapper text-center">
                        <span class="title-line-before"></span>
                        <h4 class="titles"><strong>Tech Stack and Skills</strong></h4>
                        <span class="title-line-after"></span>
                    </div>
                </div>
                <div class="row mb-2 skills-section">"""

skill_group_block = """                    <div class="col-2 list-{affix}">
                        <ul class="skill-list">
                            <li>{title}</li>
                        </ul>
                    </div>
                    <div class="col-10 list-{affix}">
                        <ul class="skill-list">
                            {skills}
                        </ul>
                    </div>"""

work_experience_headings = """                </div>
                <div class="row">
                    <div class="title-line-wrapper text-center">
                        <span class="title-line-before"></span>
                        <h4 class="titles"><strong>Work Experience</strong></h4>
                        <span class="title-line-after"></span>
                    </div>
                </div>"""

work_experience_block = """                <div class="row">
                    <div class="row">
                        <div class="col-9">
                            <h5><strong>{role}</strong> at {company}{hyperlink}</h5>
                        </div>
                        <div class="col-3 text-end">
                            <h5><em>{duration}</em></h5>
                        </div>
                    </div>
                    <div class="row">
                        <ul class="task-items-list text-justify mb-{margin_bottom}">
                            {tasks}
                        </ul>
                    </div>
                </div>"""

projects_heading = """                <div class="row">
                    <div class="title-line-wrapper text-center">
                        <span class="title-line-before"></span>
                        <h4 class="titles"><strong>Projects</strong></h4>
                        <span class="title-line-after"></span>
                    </div>
                </div>"""

project_block = """                <div class="row">
                    <div class="row">
                        <div class="col-9">
                            <h5><strong>{title}</strong>{hyperlink}</h5>
                        </div>
                        <div class="col-3 text-end">
                            <h5><em>{duration}</em></h5>
                        </div>
                    </div>
                    <div class="row">
                        <ul class="task-items-list text-justify mb-{margin_bottom}">
                            {tasks}
                        </ul>
                    </div>
                </div>"""

education_heading = """                <div class="row">
                    <div class="title-line-wrapper text-center">
                        <span class="title-line-before"></span>
                        <h4 class="titles"><strong>Education</strong></h4>
                        <span class="title-line-after"></span>
                    </div>
                </div>"""

education_block = """                <div class="row">
                    <div class="row">
                        <div class="col-9">
                            <h5><strong>{title}</strong>, <em>{institution}</em></h5>
                        </div>
                        <div class="col-3 text-end">
                            <h5><em>{duration}</em></h5>
                        </div>
                    </div>
                </div>"""

certificates_heading = """                <div class="row">
                    <div class="title-line-wrapper text-center">
                        <span class="title-line-before"></span>
                        <h4 class="titles"><strong>Certificates</strong></h4>
                        <span class="title-line-after"></span>
                    </div>
                </div>"""

certificate_block = """                <div class="row">
                    <div class="row">
                        <div class="col-9">
                            <h5><strong>{title}</strong>, <em>{institution}</em>{hyperlink}</h5>
                        </div>
                        <div class="col-3 text-end">
                            <h5><em>{date}</em></h5>
                        </div>
                    </div>
                </div>"""

hyperlink_transparency_style = """<style> a {color: #000000; text-decoration: none;}</style>"""
