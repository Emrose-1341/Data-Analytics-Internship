
 <title>Foster Care Transition Outcomes</title>
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            margin: 0;
            padding: 20px;
            color: #333;
            min-height: 100vh;
        }
        
        .container {
            max-width: 1200px;
            margin: 0 auto;
            background: rgba(255, 255, 255, 0.95);
            border-radius: 20px;
            padding: 30px;
            box-shadow: 0 20px 40px rgba(0,0,0,0.1);
        }
        
        h1 {
            text-align: center;
            color: #2c3e50;
            margin-bottom: 10px;
            font-size: 2.5em;
            font-weight: 700;
        }
        
        .subtitle {
            text-align: center;
            color: #7f8c8d;
            margin-bottom: 40px;
            font-size: 1.2em;
        }
        
        .outcome-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(500px, 1fr));
            gap: 30px;
            margin-bottom: 40px;
        }
        
        .outcome-card {
            background: white;
            border-radius: 15px;
            padding: 25px;
            box-shadow: 0 8px 25px rgba(0,0,0,0.1);
            border-left: 6px solid;
            transition: transform 0.3s ease;
        }
        
        .outcome-card:hover {
            transform: translateY(-5px);
        }
        
        .housing { border-left-color: #e74c3c; }
        .justice { border-left-color: #8b5cf6; }
        .substance { border-left-color: #f39c12; }
        .engagement { border-left-color: #27ae60; }
        
        .outcome-title {
            font-size: 1.4em;
            font-weight: 700;
            margin-bottom: 15px;
            color: #2c3e50;
        }
        
        .people-grid {
            display: grid;
            grid-template-columns: repeat(10, 1fr);
            gap: 8px;
            margin: 20px 0;
        }
        
        .person {
            width: 35px;
            height: 35px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 16px;
            transition: all 0.3s ease;
        }
        
        .person:hover {
            transform: scale(1.2);
        }
        
        .affected { background: #e74c3c; color: white; }
        .justice-affected { background: #8b5cf6; color: white; }
        .substance-affected { background: #f39c12; color: white; }
        .engaged { background: #27ae60; color: white; }
        .not-affected { background: #ecf0f1; color: #95a5a6; }
        
        .stats {
            font-size: 1.1em;
            margin-top: 15px;
            padding: 15px;
            background: #f8f9fa;
            border-radius: 8px;
        }
        
        .risk-factors {
            margin-top: 40px;
            background: white;
            border-radius: 15px;
            padding: 25px;
            box-shadow: 0 8px 25px rgba(0,0,0,0.1);
        }
        
        .risk-title {
            font-size: 1.6em;
            font-weight: 700;
            margin-bottom: 20px;
            color: #2c3e50;
            text-align: center;
        }
        
        .risk-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 20px;
        }
        
        .risk-item {
            padding: 15px;
            border-radius: 10px;
            text-align: center;
            color: white;
            font-weight: 600;
        }
        
        .extreme-risk { background: #c0392b; }
        .high-risk { background: #e74c3c; }
        .moderate-risk { background: #f39c12; }
        .protective { background: #27ae60; }
        
        .comparison {
            margin-top: 40px;
            background: white;
            border-radius: 15px;
            padding: 25px;
            box-shadow: 0 8px 25px rgba(0,0,0,0.1);
        }
        
        .comparison-title {
            font-size: 1.6em;
            font-weight: 700;
            margin-bottom: 20px;
            color: #2c3e50;
            text-align: center;
        }
        
        .comparison-row {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin: 15px 0;
            padding: 15px;
            background: #f8f9fa;
            border-radius: 10px;
        }
        
        .legend {
            display: flex;
            justify-content: center;
            gap: 30px;
            margin: 20px 0;
            flex-wrap: wrap;
        }
        
        .legend-item {
            display: flex;
            align-items: center;
            gap: 8px;
            font-weight: 600;
        }
        
        .legend-color {
            width: 20px;
            height: 20px;
            border-radius: 50%;
        }
        
        @media (max-width: 768px) {
            .outcome-grid {
                grid-template-columns: 1fr;
            }
            
            .people-grid {
                grid-template-columns: repeat(5, 1fr);
            }
            
            h1 { font-size: 2em; }
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Foster Care Transition Outcomes</h1>
        <p class="subtitle">Visual representation of post-transition experiences for Tennessee foster care youth</p>
        
        <div class="outcome-grid">
            <div class="outcome-card housing">
                <div class="outcome-title">🏠 Housing Stability</div>
                <div class="people-grid" id="housing-grid"></div>
                <div class="stats">
                    <strong>29.1% experience homelessness</strong> after leaving foster care<br>
                    <span style="color: #e74c3c;">■</span> 3 out of 10 youth face housing instability
                </div>
            </div>
            
            <div class="outcome-card justice">
                <div class="outcome-title">⚖️ Justice System Involvement</div>
                <div class="people-grid" id="justice-grid"></div>
                <div class="stats">
                    <strong>31.4% experience incarceration</strong> post-transition<br>
                    <span style="color: #8b5cf6;">■</span> Nearly 1 in 3 youth face legal system involvement
                </div>
            </div>
            
            <div class="outcome-card substance">
                <div class="outcome-title">💊 Substance Abuse Referrals</div>
                <div class="people-grid" id="substance-grid"></div>
                <div class="stats">
                    <strong>14.6% need substance abuse referrals</strong><br>
                    <span style="color: #f39c12;">■</span> About 1 in 7 youth require substance abuse support
                </div>
            </div>
            
            <div class="outcome-card engagement">
                <div class="outcome-title">💼 Work & School Engagement</div>
                <div class="people-grid" id="engagement-grid"></div>
                <div class="stats">
                    <strong>69.0% achieve work/school engagement</strong><br>
                    <span style="color: #27ae60;">■</span> About 7 out of 10 youth successfully engage in work or education
                </div>
            </div>
        </div>
        
        <div class="legend">
            <div class="legend-item">
                <div class="legend-color affected"></div>
                <span>Housing Instability</span>
            </div>
            <div class="legend-item">
                <div class="legend-color justice-affected"></div>
                <span>Justice Involvement</span>
            </div>
            <div class="legend-item">
                <div class="legend-color substance-affected"></div>
                <span>Substance Issues</span>
            </div>
            <div class="legend-item">
                <div class="legend-color engaged"></div>
                <span>Successfully Engaged</span>
            </div>
            <div class="legend-item">
                <div class="legend-color not-affected"></div>
                <span>Not Affected</span>
            </div>
        </div>
        
        <div class="risk-factors">
            <div class="risk-title">🚨 Critical Risk Factors</div>
            <div class="risk-grid">
                <div class="risk-item extreme-risk">
                    <strong>Extreme Placement Instability</strong><br>
                    (10+ placements)<br>
                    5× higher homelessness risk<br>
                    4× higher incarceration risk
                </div>
                <div class="risk-item high-risk">
                    <strong>Group Home Placement</strong><br>
                    154% higher incarceration risk<br>
                    vs. family-based care
                </div>
                <div class="risk-item moderate-risk">
                    <strong>Diagnosed Disability</strong><br>
                    87% higher homelessness risk<br>
                    65% higher incarceration risk
                </div>
                <div class="risk-item protective">
                    <strong>Female Gender</strong><br>
                    66% lower incarceration risk<br>
                    Higher work/school engagement
                </div>
            </div>
        </div>
        
        <div class="comparison">
            <div class="comparison-title">📊 Early Experience Impact</div>
            <div class="comparison-row">
                <span><strong>Early Homelessness (ages 18-19):</strong></span>
                <span style="color: #e74c3c; font-weight: bold;">62% continue to be homeless at ages 20-21</span>
            </div>
            <div class="comparison-row">
                <span><strong>Early Incarceration (ages 18-19):</strong></span>
                <span style="color: #8b5cf6; font-weight: bold;">63% remain involved with justice system</span>
            </div>
            <div class="comparison-row">
                <span><strong>Early Work/School Engagement:</strong></span>
                <span style="color: #27ae60; font-weight: bold;">53% continue engagement into early twenties</span>
            </div>
        </div>
    </div>
    
    <script>
        function createPeopleVisualization(containerId, percentage, affectedClass) {
            const container = document.getElementById(containerId);
            const totalPeople = 100;
            const affectedCount = Math.round(percentage);
            
            for (let i = 0; i < totalPeople; i++) {
                const person = document.createElement('div');
                person.className = 'person';
                
                if (i < affectedCount) {
                    person.className += ` ${affectedClass}`;
                    person.innerHTML = '👤';
                } else {
                    person.className += ' not-affected';
                    person.innerHTML = '👤';
                }
                
                container.appendChild(person);
            }
        }
        
        // Create visualizations
        createPeopleVisualization('housing-grid', 29, 'affected');
        createPeopleVisualization('justice-grid', 31, 'justice-affected');
        createPeopleVisualization('substance-grid', 15, 'substance-affected');
        createPeopleVisualization('engagement-grid', 69, 'engaged');
    </script>
</body>
</html>
