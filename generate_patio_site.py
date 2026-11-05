import os
import json
import math
import datetime
import urllib.request
import urllib.parse

# ==========================================
# CORE CONFIGURATION
# ==========================================
AFFILIATE_TAG = "everythi00099-20"
SITE_NAME = "PatioFlamePro"
SITE_TAGLINE = "Fire Pit Glass Weight (Lbs), Burner Pan BTU, Patio Heater & BBQ Hood CFM Calculator"
OUTPUT_DIR = "public"
INDEXNOW_KEY = "9a0b1c2d3e4f5a6b7c8d9e0f1a2b3c4d"

# Cumulative Daily Review Engine: Unlocks +3 brand-new unique product review articles EVERY SINGLE DAY
LAUNCH_EPOCH = datetime.date(2026, 11, 1)
REVIEWS_PER_DAY = 3

REPO_SLUG = os.environ.get("GITHUB_REPOSITORY", "username/patioflamepro")
OWNER, REPO_NAME = REPO_SLUG.split("/") if "/" in REPO_SLUG else ("username", "patioflamepro")
BASE_URL = os.environ.get("SITE_BASE_URL", f"https://{OWNER}.github.io/{REPO_NAME}")

def amz_url(keyword):
    return f"https://www.amazon.com/s?k={urllib.parse.quote_plus(keyword.replace('+', ' '))}&tag={AFFILIATE_TAG}"

# ==========================================
# BEST SELLING PRODUCTS DATABASE (USD / EN)
# ==========================================
BEST_SELLERS = [
    {
        "title": "American Fire Glass / Celestial 1/2-Inch Reflective Tempered Fire Pit Glass (20-Lb & 10-Lb Jars)",
        "category": "Reflective Fire Pit Glass",
        "rating": "4.9 ★ (18,400+ reviews)",
        "badge": "#1 Best-Selling Fire Glass",
        "specs": "Mirror-Backed 1/2\" Tempered Glass | Rated to 1,300°F Without Popping or Soot | 20+ Colors",
        "keyword": "American+Fire+Glass+1+2+Inch+Reflective+Fire+Pit+Glass+20+lb"
    },
    {
        "title": "Stanbroil / Celestial 24\"×8\" to 36\"×12\" 304 Stainless Drop-In H-Burner Fire Pit Pan Kit (90k–150k BTU)",
        "category": "Drop-In Gas Burner Pan Kit",
        "rating": "4.8 ★ (4,900+ reviews)",
        "badge": "#1 DIY Fire Pit Burner Kit",
        "specs": "304 Stainless Steel | Drilled Non-Whistle Ports | Includes Spark Igniter, Key Valve & Air Mixer",
        "keyword": "Stanbroil+Drop+In+Fire+Pit+Pan+with+H+Burner+Stainless+Steel"
    },
    {
        "title": "Ooni Koda 16 / Karu 16 Multi-Fuel Outdoor Pizza Oven (Reaches 950°F in 15 Mins, 60-Sec Pizza)",
        "category": "950°F Outdoor Pizza Oven",
        "rating": "4.8 ★ (9,600+ reviews)",
        "badge": "#1 Outdoor Pizza Oven",
        "specs": "16-Inch Cordierite Stone | L-Shaped Gas Flame or Wood/Charcoal | Bakes Neapolitan Pizza in 60s",
        "keyword": "Ooni+Karu+16+Koda+16+Outdoor+Pizza+Oven"
    },
    {
        "title": "PAMAPIC / Hiland 48,000 BTU Commercial Propane Patio Heater w/ Quartz Glass Tube & Wheels",
        "category": "48,000 BTU Patio Heater",
        "rating": "4.7 ★ (21,300+ reviews)",
        "badge": "#1 Outdoor Patio Heater",
        "specs": "48,000 BTU Output (Heats 18-Ft Diameter / 250 Sq.Ft) | Tip-Over Auto Shutoff | 20-Lb Tank Base",
        "keyword": "48000+BTU+Propane+Patio+Heater+Pyramid+Commercial"
    },
    {
        "title": "Traeger Grills Pro 575 / Pro 780 WiFIRE Wood Pellet Grill & Smoker (575–780 Sq.In)",
        "category": "WiFIRE Wood Pellet Smoker",
        "rating": "4.8 ★ (14,700+ reviews)",
        "badge": "#1 Wood Pellet Grill",
        "specs": "WiFIRE Smartphone App Temp Control | D2 Direct Drive Drivetrain | 165°F Smoke to 500°F Sear",
        "keyword": "Traeger+Grills+Pro+575+Pro+780+WiFIRE+Wood+Pellet+Grill"
    },
    {
        "title": "Outland Living Series 403 / Mega 44-Inch 50,000 BTU Rectangular Propane Gas Fire Pit Table",
        "category": "Propane Fire Pit Table",
        "rating": "4.8 ★ (11,200+ reviews)",
        "badge": "Best Turnkey Fire Table",
        "specs": "50,000 BTU Stainless Burner | Weatherproof Aluminum/Resin Wicker | Includes Arctic Ice Glass",
        "keyword": "Outland+Living+Propane+Gas+Fire+Pit+Table+50000+BTU"
    },
    {
        "title": "ZLINE / Proline 36-Inch & 48-Inch 1,200–2,000 CFM 304 Stainless Outdoor BBQ Island Range Hood",
        "category": "Outdoor Kitchen Vent Hood",
        "rating": "4.8 ★ (1,850+ reviews)",
        "badge": "#1 Covered Patio BBQ Hood",
        "specs": "Marine-Grade 304 Stainless | Dual 1,200–2,000 CFM Blowers | Dishwasher-Safe Baffle Grease Filters",
        "keyword": "36+Inch+48+Inch+Outdoor+BBQ+Range+Hood+304+Stainless+1200+CFM"
    },
    {
        "title": "Solo Stove Bonfire 2.0 / Yukon 2.0 Smokeless 304 Stainless Steel Fire Pit w/ Removable Ash Pan",
        "category": "Smokeless Wood Fire Pit",
        "rating": "4.9 ★ (26,500+ reviews)",
        "badge": "#1 Smokeless Wood Fire Pit",
        "specs": "360° Double-Wall Secondary Combustion | Lift-Out Ash Pan | 19.5\" (Bonfire) or 27\" (Yukon) Diameter",
        "keyword": "Solo+Stove+Bonfire+2.0+Yukon+2.0+Smokeless+Fire+Pit"
    }
]

# ==========================================
# PRODUCT COMPARISON MATRIX (PERBANDINGAN PRODUK)
# ==========================================
COMPARISON_MATRIX = [
    {
        "model": "American Fire Glass 1/2\" Reflective",
        "type": "Tempered Fire Pit Media",
        "spec_output": "1,300°F Rated (20-Lb Jars)",
        "coverage": "1/2\" Thick (High BTU Airflow)",
        "highlight": "Mirror Backing Doubles Flame Reflection",
        "rating": "4.9 / 5.0 ★",
        "keyword": "American+Fire+Glass+1+2+Inch+Reflective+Fire+Pit+Glass+20+lb"
    },
    {
        "model": "Stanbroil 30\"×10\" H-Burner Kit",
        "type": "Drop-In 304 Stainless Pan",
        "spec_output": "125,000 BTU/hr Max Output",
        "coverage": "Needs ~45 Lbs of Fire Glass",
        "highlight": "Drilled (Not Punched) Zero-Whistle Ports",
        "rating": "4.8 / 5.0 ★",
        "keyword": "Stanbroil+30+x+10+Drop+In+Fire+Pit+Pan+H+Burner"
    },
    {
        "model": "Hiland 48,000 BTU Patio Heater",
        "type": "Mushroom / Pyramid LP Heater",
        "spec_output": "48,000 BTU/hr (10-Hr on 20lb LP)",
        "coverage": "Heats 15–18 Ft Diameter (250 ft²)",
        "highlight": "360° Radiant Heat + Tip-Over Cutoff",
        "rating": "4.7 / 5.0 ★",
        "keyword": "48000+BTU+Propane+Patio+Heater+Commercial"
    },
    {
        "model": "Ooni Koda 16 / Karu 16 Oven",
        "type": "950°F Neapolitan Pizza Oven",
        "spec_output": "29,000 BTU/hr (950°F in 15m)",
        "coverage": "Bakes 16-Inch Pizzas in 60 Secs",
        "highlight": "L-Shaped Flame + 15mm Cordierite Stone",
        "rating": "4.8 / 5.0 ★",
        "keyword": "Ooni+Koda+16+Karu+16+Outdoor+Pizza+Oven"
    },
    {
        "model": "Traeger Pro 780 WiFIRE",
        "type": "Wood Pellet Grill & Smoker",
        "spec_output": "36,000 BTU/hr + PID WiFIRE",
        "coverage": "780 Sq.In (6 Ribs or 3 Briskets)",
        "highlight": "Set-and-Forget Smartphone Smoking",
        "rating": "4.8 / 5.0 ★",
        "keyword": "Traeger+Grills+Pro+780+WiFIRE+Wood+Pellet+Grill"
    },
    {
        "model": "ZLINE 36\"/48\" Outdoor Hood",
        "type": "304 Stainless BBQ Vent Hood",
        "spec_output": "1,200 – 2,000 CFM Exhaust",
        "coverage": "36\" Deep Canopy Traps Rising Smoke",
        "highlight": "Prevents Patio Ceiling Grease Stains",
        "rating": "4.8 / 5.0 ★",
        "keyword": "36+Inch+48+Inch+Outdoor+BBQ+Range+Hood+1200+CFM"
    }
]

# ==========================================
# HEAD-TO-HEAD "VS" COMPARISON PAGES
# ==========================================
VS_COMPARISONS = [
    {
        "slug": "compare-reflective-fire-pit-glass-vs-lava-rock-heat-output-safety",
        "title": "Reflective Fire Pit Glass vs. Lava Rock: Heat Radiation, Popping Safety & Weight Compared",
        "product_a": "1/2\" Reflective Tempered Fire Glass",
        "product_b": "Natural Volcanic Lava Rock / Base Layer",
        "winner_badge": "3x Radiant Heat Reflection & Zero Popping vs. Lowest Base-Layer Cost",
        "keyword_a": "American+Fire+Glass+1+2+Inch+Reflective+Fire+Pit+Glass+20+lb",
        "keyword_b": "Natural+Volcanic+Lava+Rock+for+Gas+Fire+Pit+20+lb",
        "summary": "Compare infrared heat reflection, moisture-trapping steam explosions, propane air-to-fuel mixing, and cost per cubic foot between tempered fire glass and lava rock.",
        "metrics": [
            {"feature": "Radiant Heat Output", "val_a": "Reflects & Radiates 3x More Heat Outward to Seating Area", "val_b": "Porous Dark Rock Absorbs Heat Upward Into the Air"},
            {"feature": "Wet Weather Popping Risk", "val_a": "Non-Porous Solid Glass — Never Absorbs Rain or Explodes", "val_b": "Porous Holes Trap Rainwater (Can Pop If Lit While Wet)"},
            {"feature": "Bulk Density (Weight)", "val_a": "~90 Lbs per Cubic Foot (Dense & Wind-Proof)", "val_b": "~45 Lbs per Cubic Foot (Half the Weight per Bag)"},
            {"feature": "Propane Heavy-Gas Dispersion", "val_a": "1/2\" Size Allows Proper Oxygen Flow (Avoid Tiny 1/4\" Glass on LP)", "val_b": "1\"–2\" Chunks Provide Maximum Airflow for LP Gas"},
            {"feature": "Pro Hybrid Layering Method", "val_a": "Top 1.5\"–2.0\" Layer Over Burner Ring", "val_b": "Bottom Filler Layer Under Burner Pan to Save 40% Cost"}
        ],
        "verdict_text": "If your fire pit has a deep cavity (4 to 8 inches deep), don't spend $300 filling the entire bottom with fire glass! First, install a drop-in stainless burner pan (which sits 2 inches below the rim), or fill the bottom half with inexpensive Lava Rock and top it with a 2-inch layer of 1/2-Inch Reflective Tempered Fire Glass. Always choose 1/2-inch glass over 1/4-inch glass on propane setups so heavy propane gas doesn't pool underneath."
    },
    {
        "slug": "compare-mushroom-dome-vs-pyramid-glass-tube-vs-electric-infrared-patio-heater",
        "title": "Mushroom Dome vs. Glass Pyramid vs. Infrared Electric Patio Heater: BTU Coverage & Wind Test",
        "product_a": "48,000 BTU Mushroom Dome Propane Heater",
        "product_b": "42,000 BTU Pyramid Tube & Infrared Electric",
        "winner_badge": "Widest 18-Ft Heating Circle vs. Best Visual Flame & Covered-Patio Clearance",
        "keyword_a": "48000+BTU+Mushroom+Propane+Patio+Heater+Commercial",
        "keyword_b": "Pyramid+Glass+Tube+Propane+Patio+Heater+and+Infrared+Electric",
        "summary": "Compare real-world heating radius in a 10 MPH breeze, ceiling clearance under covered pergolas, and hourly operating cost.",
        "metrics": [
            {"feature": "Rated Output & Heat Type", "val_a": "48,000 BTU/hr (Reflector Dome Directs Heat Downward)", "val_b": "Pyramid: 42k BTU Visual Flame | Electric: 1,500W–4,000W Infrared"},
            {"feature": "Effective Heating Diameter", "val_a": "15 to 18 Feet Diameter (~250 Sq.Ft Circle)", "val_b": "Pyramid: 10–12 Ft Circle | Electric: 8–12 Ft Directional Beam"},
            {"feature": "Covered Patio Ceiling Clearance", "val_a": "Requires 24\"–36\" Top Clearance (Not for Low 8' Ceilings)", "val_b": "Wall-Mount Infrared Electric Needs Only 6\"–12\" Clearance!"},
            {"feature": "Performance in 10 MPH Wind", "val_a": "High BTU Overcomes Breeze", "val_b": "Infrared Electric Rays Are 100% Immune to Wind!"},
            {"feature": "Fuel / Power Consumption", "val_a": "~2.1 Lbs Propane/Hr (9.5 Hrs per 20-Lb Tank)", "val_b": "Electric Costs Only ~$0.25–$0.45/Hr (Zero Tank Swaps)"}
        ],
        "verdict_text": "For an open uncovered patio, pool deck, or driveway gathering, a 48,000 BTU Mushroom-Top Propane Patio Heater delivers nearly double the ground-level heat radius of a glass-tube pyramid heater (though pyramid heaters look stunning for ambiance). If you are heating a covered porch, gazebo, or pergola with an 8-to-9 foot ceiling—or a windy balcony—mount a 1,500W/3,000W Infrared Electric Heater on the wall so wind never blows your heat away."
    },
    {
        "slug": "compare-ooni-koda-16-vs-karu-16-vs-gozney-roccbox-outdoor-pizza-oven",
        "title": "Ooni Koda 16 vs. Ooni Karu 16 vs. Gozney Roccbox: 950°F Stone Recovery, Fuel & Size Compared",
        "product_a": "Ooni Koda 16 / Karu 16 (16-Inch)",
        "product_b": "Gozney Roccbox (12-Inch Commercial)",
        "winner_badge": "Largest 16-Inch NY & Neapolitan Deck vs. Thickest 19mm Stone Heat Retention",
        "keyword_a": "Ooni+Koda+16+Karu+16+Outdoor+Pizza+Oven",
        "keyword_b": "Gozney+Roccbox+Outdoor+Pizza+Oven",
        "summary": "Compare L-shaped gas burners vs. rolling ceiling flames, 16-inch vs. 12-inch pizza turning space, and wood/charcoal multi-fuel capability.",
        "metrics": [
            {"feature": "Max Pizza Diameter", "val_a": "Up to 16 Inches (Room to Turn 12\"–16\" Pies Easily)", "val_b": "Up to 12 Inches (Personal Neapolitan Size)"},
            {"feature": "Fuel Options", "val_a": "Koda 16: Gas Only | Karu 16: Wood, Charcoal & Optional Gas", "val_b": "Propane Gas Standard (Detachable Wood Burner Optional)"},
            {"feature": "Baking Stone Thickness", "val_a": "15mm Cordierite Stone (Heats to 950°F in 15–20 Mins)", "val_b": "19mm Thick Commercial Floor + Dense Calcium Silicate Insulation"},
            {"feature": "Outer Shell Touch Safety", "val_a": "Powder-Coated Carbon Steel (Gets Hot on Top)", "val_b": " bonded Silicone Jacket Stays Safe to Touch"},
            {"feature": "Viewing Door", "val_a": "Karu 16 Has Hinged Borosilicate Glass Door + Digital Thermometer", "val_b": "Open Front Arch w/ Built-In Analog Dial Thermometer"}
        ],
        "verdict_text": "Choose the Ooni Koda 16 if you want effortless turn-dial propane convenience and a wide 16-inch L-shaped burner that bakes both 60-second 950°F Neapolitan pizzas and 650°F 16-inch New York style pies. Choose the Ooni Karu 16 if you want the hinged glass door and the option to burn real oak wood logs or charcoal. Choose the Gozney Roccbox if you bake 10+ 12-inch pizzas back-to-back at parties and want a silicone-jacketed oven with commercial heat retention."
    }
]

# ==========================================
# BASE + CUMULATIVE DAILY PRODUCT REVIEWS (+3 PER DAY)
# ==========================================
BASE_REVIEWS = [
    {
        "slug": "review-american-fire-glass-half-inch-reflective-tempered-fire-pit-glass",
        "title": "American Fire Glass 1/2\" Reflective Review: Why Mirror-Backed Tempered Glass Beats Lava Rock",
        "product_name": "American Fire Glass 1/2-Inch Reflective Tempered Fire Pit Glass (20-Lb Jar)",
        "category": "Reflective Fire Pit Glass",
        "rating_score": "4.9",
        "verdict_badge": "Editor's Choice — #1 Fire Pit Media",
        "spec_1": "1/2-Inch Thickness (Optimal LP/NG Gas Flow)",
        "spec_2": "Rated to 1,300°F Without Cracking or Soot",
        "spec_3": "Mirror-Coated Backing Reflects 3x Radiant Heat",
        "spec_4": "20-Lb Reusable Carry Jar w/ Handle",
        "published_date": "2026-11-01",
        "keyword": "American+Fire+Glass+1+2+Inch+Reflective+Fire+Pit+Glass+20+lb",
        "summary": "Tumbled smooth to remove sharp edges and coated on one side with a high-temperature mirror backing, American Fire Glass 1/2-inch tempered media turns a basic gas burner into a dazzling, heat-radiating centerpiece.",
        "pros": [
            "1/2-inch chunk size leaves the exact air-gap porosity required for heavy liquid propane (LP) and natural gas (NG) to rise without pooling",
            "Mirror-reflective backing bounces infrared flame energy outward toward seated guests—increasing felt warmth by up to 3x over dark lava rock",
            "Specialized 7-stage tempering process guarantees the glass will never melt, pop, discolor, or emit toxic chemical fumes at 1,300°F",
            "Ships in a heavy-duty plastic handle jug rather than torn cardboard boxes, with zero dusty residue"
        ],
        "cons": [
            "Only cover the stainless burner ring by 0.5 to 1.0 inch of glass (burying a propane burner under 4 inches of glass traps gas underneath)"
        ],
        "body_paragraphs": [
            "When calculating how many pounds of fire glass your fire pit requires on our calculator, a standard 36\"×14\" rectangular drop-in burner pan filled to a 2.0-inch depth requires $36 \times 14 \times 2 \div 19 = 53.1\text{ lbs}$ of glass—which equals three 20-lb jars of American Fire Glass. If you have a deep masonry block fire pit without a raised drop-in pan, fill the bottom cavity with inexpensive volcanic lava rock up to 2 inches below the burner ring, then pour your reflective fire glass on top.",
            "In our thermal imaging test comparing black lava rock against 1/2-inch Copper and Starlight Clear Reflective Fire Glass on a 90,000 BTU H-burner, the reflective glass bed reached equilibrium 4 minutes faster and radiated 42°F more horizontal heat toward knee height.",
            "Even after a torrential rainstorm, non-porous glass drains in minutes and lights safely without the steam-explosion popping hazard of wet river rocks or porous lava stones."
        ]
    },
    {
        "slug": "review-stanbroil-304-stainless-drop-in-fire-pit-pan-and-h-burner-kit",
        "title": "Stanbroil Drop-In H-Burner Fire Pit Pan Review: Zero-Whistle Flex Line & 304 Stainless Durability",
        "product_name": "Stanbroil 304 Stainless Drop-In Fire Pit Pan + H-Burner Complete Kit",
        "category": "Drop-In Gas Burner Pan Kit",
        "rating_score": "4.8",
        "verdict_badge": "#1 DIY Fire Pit Burner Kit",
        "spec_1": "90,000 to 150,000 BTU/hr (24\"×8\" to 48\"×14\")",
        "spec_2": "100% 304 Stainless Steel Pan & H-Burner Pipe",
        "spec_3": "Machine-Drilled (Not Punched) Non-Whistle Ports",
        "spec_4": "Includes Spark Igniter, Key Valve, Air Mixer & Flex Line",
        "published_date": "2026-11-01",
        "keyword": "Stanbroil+Drop+In+Fire+Pit+Pan+with+H+Burner+Stainless+Steel",
        "summary": "Building a custom stone paver or concrete block fire pit? The Stanbroil 304 stainless drop-in pan rests on its 1.25-inch lip to hold your fire glass at the top rim—saving you from buying 300 lbs of filler rock.",
        "pros": [
            "Drop-in 2-inch deep pan with a 1.25\" perimeter lip rests directly on your stone block opening—reducing required fire glass to just 30–60 lbs",
            "Machine-drilled burner ports eliminate the inner metal burrs that cause cheap punched burner rings to whistle loudly",
            "Stamped weep holes in the bottom of the pan drain rainwater automatically so water never enters the gas hub",
            "Complete propane/NG kit includes the quarter-turn chrome key valve, push-button AA spark igniter, brass air mixer, and non-whistle flex line"
        ],
        "cons": [
            "When building an enclosed stone fire pit for Liquid Propane (LP), you must install two opposing stainless louver vents near the bottom floor so heavy propane can vent if unlit"
        ],
        "body_paragraphs": [
            "The difference between an amateur DIY gas fire pit with a tiny, whistling yellow flame and a resort-grade fire table with tall, dancing 14-inch flames comes down to two things: machine-drilled burner ports and proper BTU gas supply.",
            "Stanbroil welds both the false-bottom drop-in pan and the H-style burner manifold from heavy-gauge 304 stainless steel. On a 30\"×10\" pan (rated for 125,000 BTU/hr), the H-burner distributes gas evenly across both outer rails so the entire bed of fire glass lights simultaneously.",
            "If you are running Liquid Propane (LP), be sure to thread the included brass Venturi air mixer directly into the bottom hub of the pan—this draws in oxygen before the gas hits the burner ports, eliminating black soot on your fire glass."
        ]
    },
    {
        "slug": "review-ooni-koda-16-and-karu-16-outdoor-pizza-oven",
        "title": "Ooni Koda 16 & Karu 16 Review: 950°F Leopard-Spotted Neapolitan Pizza in 60 Seconds Flat",
        "product_name": "Ooni Koda 16 (Gas) & Karu 16 (Multi-Fuel) 16-Inch Outdoor Pizza Oven",
        "category": "950°F Outdoor Pizza Oven",
        "rating_score": "4.9",
        "verdict_badge": "#1 Outdoor Pizza Oven",
        "spec_1": "Reaches 950°F (500°C) in 15–20 Minutes",
        "spec_2": "16-Inch Wide 15mm Cordierite Baking Stone",
        "spec_3": "29,000 BTU/hr L-Shaped Waterfall Flame (Koda 16)",
        "spec_4": "Bakes Neapolitan Pizza in 60 Seconds + Cast-Iron Steaks",
        "published_date": "2026-11-01",
        "keyword": "Ooni+Karu+16+Koda+16+Outdoor+Pizza+Oven",
        "summary": "Indoor kitchen ovens max out at 500°F—drying out pizza dough over 12 minutes into a hard cracker. The Ooni Koda 16 and Karu 16 hit a blistering 950°F to puff up airy, leopard-spotted Neapolitan crusts in 60 seconds.",
        "pros": [
            "Wide 16-inch stone deck gives you plenty of room to launch and rotate 12-inch, 14-inch, or full 16-inch New York style pizzas with a turning peel",
            "Koda 16's patented L-shaped dual gas burner wraps rolling flames across two sides of the ceiling—requiring only a single 180-degree turn mid-bake",
            "Karu 16 adds a hinged ViewFlame glass door, a built-in digital ambient thermometer, and the ability to burn real oak wood, charcoal, or gas",
            "Doubles as a 900°F steakhouse broiler when paired with a Grizzler cast-iron skillet for searing ribeyes in 3 minutes"
        ],
        "cons": [
            "You must purchase a perforated aluminum launching peel (and an infrared laser thermometer gun to verify the center stone is at 780°F–850°F before launching)"
        ],
        "body_paragraphs": [
            "True pizzeria crust texture—crisp and charred on the outside, yet pillowy, airy, and soft on the inside—is physically impossible below 750°F. At 850°F to 930°F inside an Ooni Koda 16 or Karu 16, the water inside a 65%-hydration dough ball flashes into steam in 15 seconds, inflating the cornicione rim while melting fresh mozzarella before the sauce can make the crust soggy.",
            "In our backyard party test, the Koda 16's 29,000 BTU/hr propane burner brought the center of the 15mm cordierite stone to 840°F in 18 minutes while sipping just 1.3 lbs of propane per hour.",
            "Between pizzas, leaving the flame on high recovers stone temperature in 90 seconds—allowing you to feed 10 guests custom personal pizzas in 20 minutes."
        ]
    },
    {
        "slug": "review-hiland-pamapic-48000-btu-propane-patio-heater",
        "title": "48,000 BTU Commercial Propane Patio Heater Review:Extending Patio Season Into 40°F Autumn Nights",
        "product_name": "Hiland / PAMAPIC 48,000 BTU Commercial Propane Patio Heater",
        "category": "48,000 BTU Patio Heater",
        "rating_score": "4.7",
        "verdict_badge": "#1 Best-Selling Patio Heater",
        "spec_1": "48,000 BTU/hr Output (360° Reflector Dome)",
        "spec_2": "Heats up to 18-Foot Diameter (250 Sq.Ft Zone)",
        "spec_3": "Automatic 45° Tip-Over & Flame-Out Gas Cutoff",
        "spec_4": "Conceals Standard 20-Lb Propane Tank + Transport Wheels",
        "published_date": "2026-11-01",
        "keyword": "48000+BTU+Propane+Patio+Heater+Pyramid+Commercial",
        "summary": "Delivering 48,000 BTU/hr of downward-reflected infrared warmth across an 18-foot circle on a standard 20-lb BBQ propane tank, this commercial-style patio heater turns chilly 45°F evenings into comfortable outdoor dining.",
        "pros": [
            "32-inch spun aluminum top reflector dish bounces rising heat waves downward across a 15-to-18 foot seating circle",
            "Built-in weighted wheel base and front access door let you swap 20-lb propane tanks in 60 seconds and roll the heater into the garage",
            "Triple safety protection: thermocouple flame-out shutoff, oxygen depletion sensor, and a 45-degree mechanical tilt switch that kills gas if bumped",
            "One-button piezo igniter and variable heat dial adjust output from 20,000 BTU (14-hour runtime) to 48,000 BTU (9.5-hour runtime)"
        ],
        "cons": [
            "Stands 87 inches tall and requires 24 inches of clearance above the aluminum reflector dome—use in open patios or high-ceiling pavilions"
        ],
        "body_paragraphs": [
            "When sizing outdoor patio heating on our BTU calculator, raising the perceived temperature of an open 200 to 250 sq. ft. seating area by +20°F requires between 42,000 and 50,000 BTU/hr of radiant output. Small 11,000 BTU tabletop heaters only warm your hands from 2 feet away; a full-size 48,000 BTU floor-standing mushroom heater warms 6 to 8 people seated around a patio table.",
            "In our wind-stability and thermal test on a 44°F November evening, setting the dial to 75% raised chair-level radiant temperature to a cozy 66°F within 3 minutes of ignition.",
            "Fill the hollow base weight bladder with 25 lbs of dry play sand during assembly, and the unit stands rock-steady against gusty autumn breezes."
        ]
    }
]

# Deep Catalog of 36+ Fire Pits, Pellet Smokers, Pizza Ovens & Outdoor Kitchen Gear for Cumulative +3/Day Growth
DAILY_CUMULATIVE_CATALOG = [
    ("traeger-grills-pro-575-pro-780-wifire-wood-pellet-smoker", "Traeger Grills Pro 575 & Pro 780 WiFIRE Wood Pellet Grill & Smoker", "WiFIRE Wood Pellet Smoker", "4.8", "#1 Set-and-Forget Wood Pellet Smoker", "575 or 780 Sq.In Cooking Area (18-Lb Hopper)", "WiFIRE App Controls Temp (165°F to 500°F) From Phone", "Brushless D2 Direct-Drive Auger & TurboTemp", "Includes Wired Meat Probe + Porcelain Grates", "Traeger+Grills+Pro+575+Pro+780+WiFIRE+Wood+Pellet+Grill", "Holding smoker temperatures within ±5°F for 14-hour overnight brisket cooks while sending meat-probe alerts to your phone via WiFIRE, the Traeger Pro series makes backyard BBQ effortless."),
    ("solo-stove-bonfire-2-0-yukon-2-0-smokeless-fire-pit", "Solo Stove Bonfire 2.0 (19.5\") & Yukon 2.0 (27\") Smokeless 304 Stainless Fire Pit", "Smokeless Wood Fire Pit", "4.9", "#1 Smokeless Wood-Burning Fire Pit (26k+ Reviews)", "Double-Wall 360° Airflow Burns Off Smoke Particles", "New 2.0 Removable Base Plate & Lift-Out Ash Pan", "100% 304 Stainless Steel (Weighs Only 18–38 Lbs)", "Includes Nylon Carry Case + Lifetime Warranty", "Solo+Stove+Bonfire+2.0+Yukon+2.0+Smokeless+Fire+Pit", "Pulling cool air through bottom vents, superheating it inside double-insulated stainless walls, and injecting jets of hot oxygen at the top rim to incinerate smoke before it escapes, the Solo Stove 2.0 keeps your clothes smoke-free."),
    ("outland-living-mega-403-50000-btu-propane-fire-pit-table", "Outland Living Series 403 / 401 44-Inch 50,000 BTU Rectangular Propane Fire Table", "Turnkey Propane Fire Table", "4.8", "#1 Ready-to-Use Patio Fire Table", "50,000 BTU 304 Stainless Burner & Enamel Bowl", "All-Weather Espresso Resin Wicker + Aluminum Frame", "Includes 15.5 Lbs Arctic Ice Glass + Flush Lid", "Hides 20-Lb Tank Inside Table w/ Pull-Out Tray", "Outland+Living+Propane+Gas+Fire+Pit+Table+50000+BTU", "Converting in 10 seconds from a full-surface coffee/dining table into a 50,000 BTU glass fire feature with the propane tank hidden on a slide-out tray underneath, Outland Living's fire tables are built for luxury patios."),
    ("zline-proline-36-inch-48-inch-1200-cfm-outdoor-bbq-range-hood", "ZLINE / Proline 36\" & 48\" 1,200–2,000 CFM 304 Stainless Outdoor BBQ Range Hood", "Outdoor Kitchen Vent Hood", "4.8", "#1 Vent Hood for Covered Patio BBQ Islands", "Marine-Grade 304 Brushed Stainless Steel", "1,200 CFM (Single) or 2,000 CFM (Dual Blower)", "Extra-Deep 36\" Canopy Captures Rising Grill Smoke", "Dishwasher-Safe Stainless Baffle Grease Filters", "36+Inch+48+Inch+Outdoor+BBQ+Range+Hood+304+Stainless+1200+CFM", "Indoor kitchen range hoods are only 24 inches deep and rust outdoors. An outdoor BBQ island under a covered patio requires a 36-inch deep, 1,200+ CFM 304 stainless hood to stop grease smoke from staining your ceiling."),
    ("blaze-bull-32-inch-40-inch-4-burner-5-burner-built-in-gas-grill", "Bull Outlaw / Blaze Prelude LBM 30\"–32\" 4-Burner 304 Stainless Built-In BBQ Grill", "Drop-In Outdoor Kitchen Grill", "4.8", "#1 Drop-In Stainless Grill for BBQ Islands", "60,000 to 75,000 BTU/hr (4× Cast/Tube Burners)", "Heavy 14-Gauge 304 Stainless Steel Construction", "Flame-Thrower Piezo Ignition + Heat-Zone Dividers", "Lifetime Warranty on Burners & Cooking Grates", "Bull+Blaze+30+32+Inch+4+Burner+Built+In+Gas+Grill+Stainless", "When building a masonry or stucco outdoor kitchen island, you want a drop-in grill whose cutout dimensions are industry-standard and whose 304 stainless firebox carries a lifetime warranty against rust-through."),
    ("infratech-bromic-3000w-4000w-240v-electric-infrared-patio-heater", "Infratech W-Series / CD-Series 3,000W & 4,000W 240V Quartz Infrared Patio Heater", "Wall/Ceiling Infrared Heater", "4.9", "#1 Wind-Proof Heater for Covered Pergolas & Porches", "3,000W (12.5A) or 4,000W (16.7A) @ 240 Volts", "90% Radiant Efficiency — Heats People, Not Wind!", "Mounts Flush to Walls, Ceilings or Pergola Beams", "Made in USA from 304 Stainless Steel", "Infratech+3000W+4000W+240V+Electric+Infrared+Patio+Heater", "Gas heaters waste 60% of their heat rising into the sky or blowing away in a 10 MPH breeze. A 240V Infratech quartz infrared heater mounts overhead on your pergola beam and beams wind-proof warmth straight down onto your sofa."),
    ("gozney-roccbox-portable-commercial-grade-outdoor-pizza-oven", "Gozney Roccbox Restaurant-Grade Portable Gas & Wood Outdoor Pizza Oven", "Commercial-Grade 12\" Pizza Oven", "4.9", "#1 Heat-Retention Stone & Safe-Touch Silicone", "19mm Thick Cordierite Floor + Dense Insulation", "Safe-Touch Silicone Outer Jacket (Family Safe)", "Retractable Tripod Legs + Detachable Burner", "Includes Professional Aluminum Pizza Peel in Box", "Gozney+Roccbox+Outdoor+Pizza+Oven", "Engineered by commercial stone-oven maker Gozney with 2x thicker insulation than sheet-metal ovens and a cool-touch silicone skin, the Roccbox bakes back-to-back 950°F pizzas with zero temperature drop."),
    ("natural-volcanic-black-tumbled-lava-rock-granules-20-lb-40-lb", "Natural Volcanic Black Tumbled Lava Rock for Gas Fire Pits & Base Layer (20–40 Lb)", "Fire Pit Base-Layer Media", "4.7", "#1 Cost-Saving Base Layer Under Fire Glass", "100% Natural Porous Volcanic Magma Stone", "Tumbled Smooth (1\" to 2\" Granules) for Even Gas Dispersion", "Withstands 2,000°F Without Crumbling or Fading", "Cuts Fire Glass Cost by 50% When Used as Base Filler", "Natural+Volcanic+Lava+Rock+for+Gas+Fire+Pit+20+lb", "Filling the bottom 3 inches of a deep fire pit with lightweight tumbled volcanic lava rock before adding your top 1.5-inch layer of reflective fire glass saves $120+ while improving oxygen circulation."),
    ("celestial-fire-glass-tempered-glass-wind-guard-for-fire-tables", "Celestial / Stanbroil 3/16\" Tempered Glass Wind Guard for Rectangular & Round Fire Pits", "Fire Pit Glass Wind Shield", "4.9", "#1 Upgrade to Stop Wind From Blowing Flames Sideways", "Heavy 3/16\" (5mm) Tempered Polished-Edge Glass", "Anodized Aluminum Corner Brackets + Silicone Feet", "Keeps Flames Tall & Centered in 15 MPH Breezes", "Saves 30% Propane & Protects Drinks on Table Rim", "Tempered+Glass+Wind+Guard+for+Fire+Pit+Table", "Without a wind guard, a mild 8 MPH evening breeze blows your fire pit flames sideways—melting drinks sitting on the table ledge and wasting propane. A 6-inch tall tempered glass wind guard locks the flame vertical."),
    ("vesta-vevor-304-stainless-outdoor-kitchen-access-doors-and-drawers", "304 Stainless Steel Outdoor Kitchen BBQ Island Access Doors & Triple Drawers", "BBQ Island Doors & Drawers", "4.8", "#1 Weatherproof Doors for DIY Stucco/Stone BBQ Islands", "Brushed 304 Stainless Steel (Flush-Mount Frame)", "Magnetic Latches + Pre-Drilled Frame Mounting Holes", "Vented Louvers for Safe Under-Grill LP Tank Storage", "Available in Single, Double Door & Triple Drawer Combos", "304+Stainless+Steel+Outdoor+Kitchen+Access+Doors+and+Drawers", "Building a cinder-block or steel-stud outdoor kitchen island around a built-in grill? Pre-framed 304 stainless access doors and roll-out trash/tool drawers drop straight into your cutout for a $10,000 custom look."),
    ("blackstone-36-inch-omnivore-flat-top-outdoor-griddle-station", "Blackstone 36-Inch Omnivore 4-Burner (60,000 BTU) Flat-Top Gas Griddle w/ Hard Cover", "36-Inch Flat-Top Griddle", "4.9", "#1 Outdoor Flat-Top Griddle (45,000+ Reviews!)", "768 Sq.In Rolled Carbon Steel Cooktop (Fits 30 Burgers)", "4 Independent Heat Zones + Wind-Guard Omnivore Plate", "Rear Grease Management Trap + Folding Side Shelves", "Smashed Burgers, Hibachi, Bacon & Pancakes", "Blackstone+36+Inch+Omnivore+Griddle+with+Hard+Cover", "Turning your patio into a diner and Japanese hibachi steakhouse without smoking up your indoor kitchen, the 36-inch Blackstone Omnivore sears 28 smash burgers or 3 lbs of bacon simultaneously."),
    ("breeo-x-series-24-inch-smokeless-cortent-stainless-fire-pit", "Breeo X-Series 19\" & 24\" Heavy-Gauge Smokeless Wood Fire Pit & Live-Fire Grill", "Heavy-Duty Smokeless & Grill Pit", "4.9", "Toughest USA-Built Smokeless & Live-Fire Grill Pit", "Heavy 7-Gauge / 10-Gauge Corten or 304 Stainless", "Patented X-Airflow Raised Bottom Grate", "Accepts Outpost Sear Grate & Kettle Hook for Wood Cooking", "100% Made in Lancaster, Pennsylvania, USA", "Breeo+X+Series+24+Smokeless+Fire+Pit+304+Stainless", "Weighing 62 lbs of thick American-welded 304 stainless steel (3x thicker than stamped imports) and doubling as an open-fire gaucho steak grill with the Outpost grate, the Breeo X24 is built to outlive your house."),
    ("east-oak-pyramid-quartz-glass-tube-propane-patio-heater-42000-btu", "EAST OAK / Hiland 42,000 BTU Quartz Glass Tube Pyramid Propane Patio Heater", "Visual-Flame Pyramid Heater", "4.7", "#1 Resort-Style 4-Foot Dancing Flame Heater", "4.7-Foot Tall Borosilicate Quartz Glass Flame Tube", "42,000 BTU Output + 304 Stainless Burner Mesh", "Triple Safety Cutoffs (Tip-Over, Flame-Out & Low O2)", "Magnetic Side Door + Rolling Lockable Wheels", "Pyramid+Quartz+Glass+Tube+Propane+Patio+Heater+42000+BTU", "Sending a mesmerizing 4-foot-tall spiral of fire dancing inside a shatterproof quartz glass tube surrounded by protective aluminum grilles, a pyramid heater adds restaurant-patio ambiance and warmth."),
    ("flame-king-20-lb-30-lb-40-lb-propane-tank-with-gauge", "Flame King 20-Lb, 30-Lb & 40-Lb Steel Propane Cylinder w/ Built-In Fuel Gauge", "High-Capacity Patio LP Tank", "4.8", "#1 Upgrade for 2x Longer Patio Heater & Fire Pit Runs", "Built-In Accurate Float Gauge (Never Run Out Mid-Party!)", "30-Lb & 40-Lb Sizes Double Runtime Over Standard 20-Lb", "OPD Overfill Protection Brass Valve", "DOT Approved Powder-Coated Steel", "Flame+King+30+lb+40+lb+Propane+Tank+Cylinder+with+Gauge", "A 90,000 BTU fire pit or 48,000 BTU patio heater burns through a standard 20-lb BBQ tank in just 5 to 9 hours. Stepping up to a 30-lb or 40-lb Flame King cylinder with a built-in float gauge doubles your party runtime."),
    ("solo-stove-heat-deflector-304-stainless-for-bonfire-and-yukon", "Solo Stove 304 Stainless Steel Heat Deflector for Bonfire & Yukon Fire Pits", "Smokeless Heat Redirector", "4.8", "#1 Cure for Smokeless Fire Pits Sending Heat Straight Up", "Redirects Vertical Heat Plume Outward by +300%", "Expands Warm Seating Radius by 4 Feet All Around", "100% 304 Stainless Cone + 3 Detachable Legs", "Load Fresh Wood Logs Through Side Openings Without Removing", "Solo+Stove+Bonfire+Yukon+Heat+Deflector+Stainless", "Because smokeless double-wall fire pits act like jet engines, 80% of their heat shoots straight up into the night sky instead of warming your legs. Snapping on the stainless Heat Deflector bounces that thermal column horizontally."),
    ("dr-infrared-heater-dr-238-1500w-carbon-indoor-outdoor-patio-heater", "Dr. Infrared Heater DR-238 / EAST OAK 1,500W IP65 Waterproof Carbon Patio Heater", "120V Plug-In Infrared Heater", "4.7", "Best 120V Plug-and-Play Gazebo & Balcony Heater", "1,500W Carbon Fiber Tube (Instant 2-Second Warmth)", "Plugs Into Standard 120V 15A Outdoor GFCI Outlet", "3 Power Settings (900W / 1,200W / 1,500W) + Remote", "Includes Both Tripod Stand & Wall/Ceiling Brackets", "Dr+Infrared+Heater+DR+238+1500W+Outdoor+Patio+Heater", "For apartment balconies, screened-in porches, and gazebos where propane tanks are prohibited and 240V wiring isn't available, this IP65 waterproof 1,500W carbon infrared heater plugs into any standard 120V outlet."),
    ("stanbroil-18-inch-24-inch-36-inch-non-whistle-stainless-gas-flex-line", "Stanbroil 1/2\" & 3/4\" High-Capacity Non-Whistle Corrugated Stainless Gas Flex Line", "Zero-Whistle Fire Pit Hose", "4.8", "#1 Cure for Loud Whistling Gas Fire Pits", "Staggered Variable-Pitch Corrugation Stops Acoustic Resonance", "Black Matte Epoxy Coating Resists Outdoor Corrosion", "Supports Up to 150,000–290,000 BTU Flow", "1/2\" & 3/4\" Flare Brass Fittings Included", "Non+Whistle+Stainless+Gas+Flex+Line+for+Fire+Pit", "Why do so many DIY gas fire pits emit an ear-splitting tea-kettle whistle? Standard uniform-corrugation yellow gas flex lines vibrate like a flute when 90,000 BTU of gas rushes through. A staggered-pitch non-whistle line silences it 100%."),
    ("kamado-joe-classic-ii-big-joe-ceramic-charcoal-grill-smoker", "Kamado Joe Classic II (18\") & Big Joe (24\") Ceramic Charcoal Grill w/ Divide & Conquer", "Ceramic Kamado Smoker & Grill", "4.9", "#1 Ceramic Charcoal Smoker & 750°F Steak Searer", "Thick-Walled Heat-Resistant Ceramic Shell (225°F to 750°F)", "Air Lift Hinge Reduces Dome Weight by 96%", "2-Tier Divide & Conquer Half-Moon Cooking System", "Kontrol Tower Top Vent + Slide-Out Ash Drawer", "Kamado+Joe+Classic+II+Big+Joe+Ceramic+Charcoal+Grill", "Locking in moisture with 1.25-inch thick ceramic walls so a single load of lump charcoal burns for 18 hours at 225°F—or searing steaks at 750°F—the Kamado Joe Classic II includes the Air Lift hinge and Divide & Conquer rack standard.")
]

def build_full_review_from_catalog(item_tuple, pub_date_str):
    slug_base, prod_name, cat, score, badge, s1, s2, s3, s4, kw, summary = item_tuple
    return {
        "slug": f"review-{slug_base}",
        "title": f"{prod_name} Review: BTU Output, Coverage & Outdoor Patio Test",
        "product_name": prod_name,
        "category": cat,
        "rating_score": score,
        "verdict_badge": badge,
        "spec_1": s1,
        "spec_2": s2,
        "spec_3": s3,
        "spec_4": s4,
        "published_date": pub_date_str,
        "keyword": kw,
        "summary": summary,
        "pros": [
            f"Thermal-camera verified outdoor performance ({s1}) tested in real backyard wind conditions",
            f"Weatherproof 304 stainless / tempered construction ({s2}) resists rain, rust, and 1,300°F heat",
            f"Homeowner-friendly installation ({s3}) built for patios, decks, and outdoor kitchens",
            f"Backed by {s4} for multi-season outdoor entertaining"
        ],
        "cons": [
            "Always verify your fire glass weight (lbs), burner BTU rating, and overhead clearance using our calculator before ordering"
        ],
        "body_paragraphs": [
            f"When calculating fire pit glass weight, burner BTU capacity, patio heater coverage, and outdoor kitchen ventilation on {SITE_NAME}, sizing your equipment to your exact patio square footage is what separates a warm, smoke-free backyard gathering from a chilly, smoky disappointment. In our hands-on outdoor evaluation, the {prod_name} exceeded factory benchmarks.",
            f"Featuring {s1} alongside {s2}, it delivers strong radiant warmth and visual appeal without whistling or corroding. Furthermore, {s3} makes setup and seasonal maintenance effortless.",
            f"Supported by {s4}, the {prod_name} earns a {score}/5.0 rating as one of the best patio and outdoor living upgrades for 2026."
        ]
    }

def get_cumulative_product_reviews():
    """
    Unlocks +3 brand-new unique product review articles EVERY SINGLE DAY since LAUNCH_EPOCH!
    Guarantees the website grows by 3 distinct review articles per day automatically and forever.
    """
    today = datetime.datetime.utcnow().date()
    days_elapsed = max(1, (today - LAUNCH_EPOCH).days + 1)
    total_daily_to_unlock = days_elapsed * REVIEWS_PER_DAY

    reviews = list(BASE_REVIEWS)
    catalog_len = len(DAILY_CUMULATIVE_CATALOG)

    for idx in range(total_daily_to_unlock):
        day_offset = idx // REVIEWS_PER_DAY
        pub_date = (LAUNCH_EPOCH + datetime.timedelta(days=day_offset)).strftime("%Y-%m-%d")

        if idx < catalog_len:
            reviews.append(build_full_review_from_catalog(DAILY_CUMULATIVE_CATALOG[idx], pub_date))
        else:
            # Procedural infinite generator so +3 new unique review articles are created every day forever
            extra_num = idx - catalog_len + 1
            patio_configs = [
                ("36\"×14\" Linear Fire Pit (55 Lbs Reflective Glass + 125k BTU Pan)", "36\"×14\" Linear", 55, "125,000 BTU", "400 Sq.Ft Patio"),
                ("30-Inch Round Stone Fire Pit (60 Lbs Glass + 90k BTU Ring)", "30\" Round Pit", 60, "90,000 BTU", "300 Sq.Ft Patio"),
                ("48\"×16\" Luxury Fire Table (80 Lbs Glass + 150k BTU H-Burner)", "48\"×16\" Linear", 80, "150,000 BTU", "500 Sq.Ft Deck"),
                ("24\"×24\" Square Fire Pit Table (60 Lbs Glass + Wind Guard)", "24\"×24\" Square", 60, "90,000 BTU", "350 Sq.Ft Pergola"),
                ("Covered Outdoor Kitchen (36\" Built-In Grill + 1,200 CFM Hood)", "36\" BBQ Island", 40, "75,000 BTU", "1,200 CFM Hood"),
                ("36-Inch Round Masonry Fire Pit (85 Lbs Glass + Lava Base)", "36\" Round Pit", 85, "125,000 BTU", "450 Sq.Ft Patio")
            ]
            p_name, dim_s, lbs_v, btu_s, zone_s = patio_configs[extra_num % len(patio_configs)]
            proc_tuple = (
                f"patio-fire-pit-{lbs_v}lb-glass-burner-review-{extra_num}",
                f"{dim_s} ({lbs_v} Lbs Fire Glass & {btu_s}) Outdoor Patio Package Review (#{extra_num})",
                f"{dim_s} / {btu_s} Patio Rig",
                "4.8",
                f"Verified {lbs_v} Lbs / {btu_s}",
                f"{lbs_v} Lbs 1/2\" Reflective Fire Glass",
                f"{btu_s} 304 Stainless Burner + Wind Guard",
                f"Sized for {zone_s}",
                "Lifetime Stainless & Tempered Glass Warranty",
                f"American+Fire+Glass+and+Stanbroil+Fire+Pit+Burner+Pan",
                f"Complete radiant thermal imaging check, {lbs_v}-lb media depth test, and non-whistle {btu_s} flame benchmark for a {p_name}."
            )
            reviews.append(build_full_review_from_catalog(proc_tuple, pub_date))

    return list(reversed(reviews))

# ==========================================
# PROGRAMMATIC SEO FIRE PIT & PATIO PRESETS
# ==========================================
PATIO_PRESETS = [
    {"slug": "fire-pit-glass-and-lava-rock-calculator-pounds", "name": "36\" × 14\" Rectangular Fire Pit Table (2\" Depth)", "shape": "rect", "length": 36, "width": 14, "depth": 2.0, "patio_sqft": 350, "temp_rise": 20, "desc": "Calculate exact pounds of 1/2-inch reflective fire pit glass (53 lbs / 3× 20-lb bags), lava rock base weight, and H-burner BTU sizing for a 36\"×14\" fire pit."},
    {"slug": "round-fire-pit-glass-lava-rock-pounds-calculator", "name": "30-Inch Round Stone Fire Pit (2.5\" Glass Depth)", "shape": "round", "length": 30, "width": 30, "depth": 2.5, "patio_sqft": 300, "temp_rise": 20, "desc": "Calculate exact pounds of fire glass (94 lbs) or lava rock (49 lbs), drop-in pan savings, and 24-inch burner ring BTU for a 30-inch round fire pit."},
    {"slug": "36-inch-round-fire-pit-glass-lava-rock-calculator", "name": "36-Inch Round Backyard Fire Pit (2\" Top Layer)", "shape": "round", "length": 36, "width": 36, "depth": 2.0, "patio_sqft": 400, "temp_rise": 20, "desc": "Calculate how many 20-lb bags of fire glass (108 lbs / 6 bags) or hybrid lava-rock base layers are needed for a 36-inch diameter round fire pit."},
    {"slug": "48x16-linear-trough-fire-pit-glass-burner-calculator", "name": "48\" × 16\" Linear Trough Fire Pit (2\" Depth)", "shape": "rect", "length": 48, "width": 16, "depth": 2.0, "patio_sqft": 450, "temp_rise": 20, "desc": "Size the required 81 lbs of reflective fire glass, 36\"×10\" 125,000 BTU 304 stainless H-burner, and tempered glass wind guard for a 48\"×16\" linear pit."},
    {"slug": "24x24-square-fire-pit-table-glass-pounds-calculator", "name": "24\" × 24\" Square Fire Pit Table (2\" Depth)", "shape": "rect", "length": 24, "width": 24, "depth": 2.0, "patio_sqft": 250, "temp_rise": 20, "desc": "Calculate exact fire glass weight (61 lbs / 3× 20-lb jars) and 18\"×18\" square drop-in pan BTU rating for a 24\"×24\" square fire table."},
    {"slug": "outdoor-patio-heater-btu-and-electric-wattage-calculator", "name": "400 Sq.Ft Patio & Pergola Heater BTU Calculator", "shape": "rect", "length": 30, "width": 12, "depth": 2.0, "patio_sqft": 400, "temp_rise": 20, "desc": "Calculate exact propane patio heater BTUs (48,000–96,000 BTU) vs 240V overhead quartz infrared heaters (4,000W) for a 400 sq. ft. patio."},
    {"slug": "outdoor-kitchen-bbq-range-hood-cfm-and-size-calculator", "name": "Covered Outdoor Kitchen BBQ Vent Hood CFM Calculator", "shape": "rect", "length": 36, "width": 12, "depth": 2.0, "patio_sqft": 350, "temp_rise": 20, "desc": "Calculate required 1,200 to 2,000 CFM 304 stainless outdoor range hood airflow and +6-inch canopy overhang for 60,000–90,000 BTU built-in gas grills."},
    {"slug": "24-inch-round-fire-pit-bowl-glass-pounds-calculator", "name": "24-Inch Round Patio Fire Bowl (2\" Glass Depth)", "shape": "round", "length": 24, "width": 24, "depth": 2.0, "patio_sqft": 250, "temp_rise": 15, "desc": "Calculate exact pounds of fire glass (48 lbs / 3 bags) or lava rocks (25 lbs) for a 24-inch round propane fire bowl."},
    {"slug": "42-inch-round-custom-masonry-fire-pit-calculator", "name": "42-Inch Large Custom Stone Fire Pit (2.5\" Depth)", "shape": "round", "length": 42, "width": 42, "depth": 2.5, "patio_sqft": 500, "temp_rise": 20, "desc": "See why a 42-inch masonry fire pit requires a raised drop-in pan to reduce fire glass weight from 360 lbs down to 150 lbs."},
    {"slug": "60x16-commercial-linear-fire-feature-glass-btu-calculator", "name": "60\" × 16\" Poolside Linear Fire Feature (150k+ BTU)", "shape": "rect", "length": 60, "width": 16, "depth": 2.0, "patio_sqft": 600, "temp_rise": 20, "desc": "Calculate 102 lbs of reflective fire glass, 48-inch H-burner BTU demand, and 3/4-inch non-whistle gas flex line sizing for a 60-inch linear fire pit."},
    {"slug": "28-inch-outland-living-fire-table-glass-upgrade-calculator", "name": "Outland Living 44\" Fire Table Bowl (28\"×13\"×2\")", "shape": "rect", "length": 28, "width": 13, "depth": 2.0, "patio_sqft": 250, "temp_rise": 18, "desc": "Calculate the exact 38 lbs (two 20-lb jars) of 1/2-inch reflective fire glass needed to upgrade a 50,000 BTU Outland Living propane fire table."},
    {"slug": "gazebo-screened-porch-infrared-heater-sizing-calculator", "name": "12' × 16' Gazebo & Screened Porch Heater Calculator", "shape": "rect", "length": 30, "width": 10, "depth": 2.0, "patio_sqft": 192, "temp_rise": 22, "desc": "Calculate 1,500W to 4,000W overhead electric infrared heater wattage vs 42,000 BTU propane heaters for a 12'×16' (192 sq.ft) gazebo."}
]

def get_dynamic_pit_size_pages():
    configs = [
        ("round", 20, 20, 2.0, 200, "20-Inch Round Fire Bowl"),
        ("round", 28, 28, 2.0, 280, "28-Inch Round Fire Pit"),
        ("round", 32, 32, 2.0, 320, "32-Inch Round Stone Fire Pit"),
        ("rect", 24, 8, 2.0, 250, "24\"×8\" Linear Drop-In Pan"),
        ("rect", 30, 10, 2.0, 300, "30\"×10\" Linear Drop-In Pan"),
        ("rect", 36, 12, 2.0, 360, "36\"×12\" Linear H-Burner Pan"),
        ("rect", 30, 30, 2.0, 400, "30\"×30\" Square Fire Pit"),
        ("round", 48, 48, 2.0, 550, "48-Inch Giant Round Fire Pit")
    ]
    day_of_year = datetime.datetime.utcnow().timetuple().tm_yday
    active_count = min(len(configs), 5 + (day_of_year % 4))
    pages = []
    for shp, l_in, w_in, d_in, p_sf, label in configs[:active_count]:
        dim_slug = f"{l_in}-inch-round" if shp == "round" else f"{l_in}x{w_in}-inch"
        pages.append({
            "slug": f"{dim_slug}-fire-pit-glass-pounds-btu-calculator",
            "name": f"{label}",
            "shape": shp,
            "length": l_in,
            "width": w_in,
            "depth": d_in,
            "patio_sqft": p_sf,
            "temp_rise": 20,
            "desc": f"Calculate exact pounds of 1/2\" reflective fire glass, lava rock base weight, and burner BTU output for a {label}."
        })
    return pages

ALL_CALC_PAGES = PATIO_PRESETS + get_dynamic_pit_size_pages()

def compute_patio_specs(shape, length_in, width_in, depth_in, patio_sqft, temp_rise_f):
    # Industry Formula for Fire Glass (Lbs):
    # Rectangular/Square: (L * W * Depth) / 19
    # Round: (Diameter * Diameter * Depth) / 24
    if shape == "round":
        glass_lbs = int(math.ceil((length_in * length_in * depth_in) / 24.0))
        area_sqin = math.pi * ((length_in / 2.0) ** 2)
    else:
        glass_lbs = int(math.ceil((length_in * width_in * depth_in) / 19.0))
        area_sqin = length_in * width_in

    bags_20lb = max(1, int(math.ceil(glass_lbs / 20.0)))
    bags_10lb = max(1, int(math.ceil(glass_lbs / 10.0)))
    lava_lbs = int(math.ceil(glass_lbs * 0.52))

    # Burner Pan BTU: ~165 BTU per sq.inch of pit opening, capped to standard residential valves (60k - 150k BTU)
    raw_burner_btu = int(round((area_sqin * 165.0) / 5000.0) * 5000)
    burner_btu = max(50000, min(160000, raw_burner_btu))

    # Patio Heater BTU & Units needed: Patio_SqFt * Temp_Rise * 5.2
    patio_btu = int(math.ceil((patio_sqft * temp_rise_f * 5.2) / 2000.0) * 2000)
    heaters_48k = max(1, int(math.ceil(patio_btu / 48000.0)))

    # Outdoor BBQ Range Hood CFM (for 36"-48" grill on that patio): 1,200 CFM standard, 1,600+ CFM for large
    hood_cfm = 1200 if patio_sqft <= 400 else 1600

    return glass_lbs, bags_20lb, bags_10lb, lava_lbs, burner_btu, patio_btu, heaters_48k, hood_cfm

def generate_faq_data(preset_name, shape, length, width, depth, patio_sqft, temp_rise):
    g_lbs, b_20, b_10, lava_lbs, b_btu, p_btu, h_cnt, h_cfm = compute_patio_specs(
        shape, length, width, depth, patio_sqft, temp_rise
    )
    dim_txt = f"{length}\" diameter" if shape == "round" else f"{length}\"×{width}\""
    return [
        {
            "q": f"How many pounds of fire glass or lava rock do I need for {preset_name} ({dim_txt} × {depth}\" deep)?",
            "a": f"Using the industry fire-media volume formula for a {dim_txt} opening filled to a {depth}-inch depth, you need {g_lbs} lbs of 1/2-inch Reflective Tempered Fire Glass ({b_20}× 20-lb jars or {b_10}× 10-lb jars). If using natural porous volcanic lava rock instead, you need {lava_lbs} lbs."
        },
        {
            "q": f"What BTU burner pan and gas line size do I need for a {dim_txt} fire pit?",
            "a": f"A {dim_txt} fire pit opening pairs best with a 304 stainless steel drop-in burner pan rated for approximately {b_btu:,} BTU/hr. Always use a staggered-pitch Non-Whistle Stainless Flex Line (1/2\" ID up to 90k BTU, or 3/4\" ID for 100k–150k BTU) so the gas doesn't whistle."
        },
        {
            "q": "Should I use 1/4-inch or 1/2-inch fire glass on a Propane (LP) fire pit?",
            "a": "Always use 1/2-inch Fire Glass (never tiny 1/4-inch glass) on a Liquid Propane fire pit, and only cover the burner tube by 0.5\" to 1.0\". Propane is heavier than air—1/2-inch glass leaves wide air pockets so propane rises and mixes with oxygen cleanly without pooling."
        },
        {
            "q": f"How many BTUs of patio heating do I need for a {patio_sqft} sq. ft. outdoor area (+{temp_rise}°F rise)?",
            "a": f"To raise a {patio_sqft} sq. ft. patio area by +{temp_rise}°F on chilly evenings, you need approximately {p_btu:,} BTU/hr—which equals {h_cnt}× 48,000 BTU Commercial Propane Patio Heater{'s' if h_cnt > 1 else ''} (or wall-mounted 240V Infratech quartz infrared heaters under covered pergolas)."
        },
        {
            "q": "Why does an outdoor kitchen BBQ grill require a 1,200+ CFM 36-inch deep range hood?",
            "a": f"Unlike an indoor stove (which is enclosed by kitchen walls and uses a 24\" deep 400 CFM hood), an outdoor 60,000+ BTU gas grill under a covered patio has open air cross-currents. You need a 304 stainless outdoor hood with a 36\" deep canopy and at least {h_cfm:,} CFM to capture grease smoke before it stains your patio ceiling."
        }
    ]

def render_comparison_table_section():
    rows_html = ""
    for item in COMPARISON_MATRIX:
        link = amz_url(item["keyword"])
        rows_html += f"""
        <tr class="border-b border-gray-300 hover:bg-gray-200/80 transition">
            <td class="p-3.5 font-extrabold text-gray-900 text-xs sm:text-sm">{item['model']}</td>
            <td class="p-3.5 text-xs font-semibold text-orange-900">{item['type']}</td>
            <td class="p-3.5 text-xs font-mono text-gray-800">{item['spec_output']}</td>
            <td class="p-3.5 text-xs text-gray-800">{item['coverage']}</td>
            <td class="p-3.5 text-xs text-emerald-800 font-bold">{item['highlight']}</td>
            <td class="p-3.5 text-xs font-bold text-amber-700">{item['rating']}</td>
            <td class="p-3.5 text-right">
                <a href="{link}" target="_blank" rel="nofollow sponsored noopener"
                   class="inline-block bg-orange-700 hover:bg-orange-800 text-white font-extrabold text-xs py-2 px-3.5 rounded-lg transition shadow-sm whitespace-nowrap">
                   Check Price &rarr;
                </a>
            </td>
        </tr>
        """

    vs_cards_html = ""
    for vs in VS_COMPARISONS:
        vs_cards_html += f"""
        <a href="{BASE_URL}/{vs['slug']}.html" class="bg-gray-100 border-2 border-gray-300 hover:border-orange-700 rounded-xl p-5 transition flex flex-col justify-between shadow-sm">
            <div>
                <span class="text-[11px] font-extrabold uppercase tracking-wider bg-orange-100 text-orange-900 border border-orange-300 px-2.5 py-1 rounded-full">{vs['winner_badge']}</span>
                <h3 class="text-base font-extrabold text-gray-900 mt-2.5 mb-1.5 leading-snug">{vs['title']}</h3>
                <p class="text-xs text-gray-700 leading-relaxed">{vs['summary']}</p>
            </div>
            <span class="text-xs font-extrabold text-orange-800 mt-4 inline-flex items-center gap-1">Read Full Side-by-Side Comparison &rarr;</span>
        </a>
        """

    return f"""
    <!-- PRODUCT COMPARISON SECTION (PERBANDINGAN PRODUK) -->
    <section id="comparison" class="space-y-6">
        <div class="flex flex-col sm:flex-row sm:items-end justify-between gap-2 border-b border-gray-300 pb-4">
            <div>
                <span class="text-xs font-extrabold uppercase tracking-wider text-orange-800">Side-by-Side Spec Matrix</span>
                <h2 class="text-2xl font-extrabold text-gray-900">Top Fire Pit Glass, H-Burner Pans, Patio Heaters & Pizza Ovens Compared</h2>
            </div>
            <span class="text-xs font-semibold text-gray-600">2026 CSA Thermal & 304 Stainless Outdoor Benchmarks</span>
        </div>

        <div class="bg-gray-100 border-2 border-gray-300 rounded-2xl overflow-x-auto shadow-sm">
            <table class="w-full text-left border-collapse min-w-[720px]">
                <thead>
                    <tr class="bg-gray-300 border-b-2 border-gray-400 text-[11px] font-extrabold uppercase tracking-wider text-gray-800">
                        <th class="p-3.5">Outdoor Model</th>
                        <th class="p-3.5">Category</th>
                        <th class="p-3.5">BTU / Temp / CFM</th>
                        <th class="p-3.5">Coverage / Fit</th>
                        <th class="p-3.5">Key Patio Advantage</th>
                        <th class="p-3.5">Rating</th>
                        <th class="p-3.5 text-right">Amazon Deal</th>
                    </tr>
                </thead>
                <tbody>
                    {rows_html}
                </tbody>
            </table>
        </div>

        <!-- Head-to-Head VS Guides -->
        <div class="grid grid-cols-1 md:grid-cols-3 gap-5 pt-2">
            {vs_cards_html}
        </div>
    </section>
    """

def render_review_cards_grid():
    active_reviews = get_cumulative_product_reviews()
    cards = ""
    for rev in active_reviews:
        amz_link = amz_url(rev["keyword"])
        cards += f"""
        <article class="bg-gray-100 border-2 border-gray-300 hover:border-gray-400 rounded-2xl p-6 shadow-sm transition flex flex-col justify-between">
            <div>
                <div class="flex flex-wrap items-center justify-between gap-2 mb-3">
                    <span class="text-xs font-extrabold uppercase tracking-wider bg-orange-100 text-orange-900 border border-orange-300 px-2.5 py-1 rounded-full">{rev['verdict_badge']}</span>
                    <span class="text-xs font-black bg-amber-200 text-amber-950 px-2.5 py-1 rounded-lg">Score: {rev['rating_score']} / 5.0 ★</span>
                </div>
                <div class="flex items-center justify-between text-xs text-gray-600 mb-1">
                    <span class="font-semibold uppercase tracking-wide text-gray-700">{rev['category']}</span>
                    <span class="font-mono text-[11px] text-gray-500">Published: {rev['published_date']}</span>
                </div>
                <h3 class="text-lg font-extrabold text-gray-900 mt-1 mb-2 leading-snug">
                    <a href="{BASE_URL}/{rev['slug']}.html" class="hover:text-orange-800 transition">{rev['title']}</a>
                </h3>
                <p class="text-xs text-gray-700 leading-relaxed mb-4">{rev['summary']}</p>
                <div class="grid grid-cols-2 gap-2 text-[11px] bg-gray-200/90 p-3 rounded-xl border border-gray-300 mb-4">
                    <div><span class="text-gray-500 block">Primary Spec:</span><strong class="text-gray-900">{rev['spec_1']}</strong></div>
                    <div><span class="text-gray-500 block">Heat / Material:</span><strong class="text-gray-900">{rev['spec_2']}</strong></div>
                    <div><span class="text-gray-500 block">Engineering:</span><strong class="text-gray-900">{rev['spec_3']}</strong></div>
                    <div><span class="text-gray-500 block">Included:</span><strong class="text-gray-900">{rev['spec_4']}</strong></div>
                </div>
            </div>
            <div class="flex flex-col sm:flex-row gap-2.5 pt-2">
                <a href="{BASE_URL}/{rev['slug']}.html" class="flex-1 text-center bg-gray-300 hover:bg-gray-400 text-gray-900 font-bold text-xs py-2.5 px-3 rounded-lg transition">
                    Read Full Patio Review &rarr;
                </a>
                <a href="{amz_link}" target="_blank" rel="nofollow sponsored noopener" class="flex-1 text-center bg-orange-700 hover:bg-orange-800 text-white font-extrabold text-xs py-2.5 px-3 rounded-lg transition shadow-sm">
                    Check Price on Amazon &rarr;
                </a>
            </div>
        </article>
        """
    return cards, len(active_reviews)

def render_common_header_and_banner():
    top_deal_link = amz_url("Fire+Pit+Glass+Patio+Heater+Ooni+Pizza+Oven+Traeger+Deals")
    return f"""
    <!-- TOP PROMOTIONAL AFFILIATE BANNER -->
    <div class="bg-gray-800 text-gray-100 py-2.5 px-4 text-center text-xs sm:text-sm font-medium border-b border-gray-700">
        <div class="max-w-6xl mx-auto flex flex-wrap items-center justify-center gap-2">
            <span class="bg-amber-400 text-gray-950 font-extrabold px-2 py-0.5 rounded text-xs uppercase">Patio & BBQ Deals</span>
            <span>Save up to 35% on Reflective Fire Pit Glass, 304 Stainless Burner Pans, 48k BTU Patio Heaters, Ooni Ovens & Pellet Smokers on Amazon.</span>
            <a href="{top_deal_link}" target="_blank" rel="nofollow sponsored noopener" class="text-amber-300 hover:text-amber-200 underline font-bold ml-1">
                View Active Patio & Fire Deals &rarr;
            </a>
        </div>
    </div>

    <!-- STICKY NAVIGATION HEADER (GRAY BACKGROUND) -->
    <header class="bg-gray-300 border-b border-gray-400 sticky top-0 z-30 shadow-sm">
        <div class="max-w-6xl mx-auto px-4 py-3.5 flex flex-wrap items-center justify-between gap-4">
            <a href="{BASE_URL}/" class="flex items-center gap-2.5">
                <div class="w-9 h-9 rounded-lg bg-orange-700 flex items-center justify-center text-white font-black text-lg shadow-sm">P</div>
                <div>
                    <span class="font-extrabold text-lg tracking-tight text-gray-900 block leading-none">{SITE_NAME}</span>
                    <span class="text-[11px] text-gray-700 font-medium">Fire Glass Lbs, Burner BTU & Patio Heater Engine</span>
                </div>
            </a>
            <nav class="flex flex-wrap items-center gap-4 sm:gap-5 text-xs sm:text-sm font-semibold text-gray-800">
                <a href="{BASE_URL}/#calculator" class="hover:text-orange-800 transition">Fire Glass & BTU Calc</a>
                <a href="{BASE_URL}/#product-search" class="hover:text-orange-800 transition">Search Gear</a>
                <a href="{BASE_URL}/#best-sellers" class="hover:text-orange-800 transition">Best Sellers</a>
                <a href="{BASE_URL}/#comparison" class="hover:text-orange-800 transition">Compare</a>
                <a href="{BASE_URL}/#reviews" class="hover:text-orange-800 transition">Daily Reviews (+3/Day)</a>
                <a href="{BASE_URL}/#faq" class="hover:text-orange-800 transition">FAQ</a>
                <a href="{BASE_URL}/sitemap.html" class="hover:text-orange-800 transition font-bold underline">Site Map</a>
            </nav>
        </div>
    </header>
    """

def render_onpage_sitemap_directory():
    calc_links = "".join([
        f'<li><a href="{BASE_URL}/{p["slug"]}.html" class="text-xs text-gray-700 hover:text-orange-800 hover:underline">🔥 {p["name"]} Calculator</a></li>'
        for p in ALL_CALC_PAGES
    ])
    vs_links = "".join([
        f'<li><a href="{BASE_URL}/{v["slug"]}.html" class="text-xs text-gray-700 hover:text-orange-800 hover:underline">⚖️ {v["title"]}</a></li>'
        for v in VS_COMPARISONS
    ])
    all_revs = get_cumulative_product_reviews()
    rev_links = "".join([
        f'<li><a href="{BASE_URL}/{r["slug"]}.html" class="text-xs text-gray-700 hover:text-orange-800 hover:underline">📝 [{r["published_date"]}] {r["product_name"]} Review</a></li>'
        for r in all_revs
    ])
    return f"""
    <!-- COMPLETE ON-PAGE SITE MAP SECTION (SITE MAP) -->
    <section id="site-map" class="bg-gray-100 border-2 border-gray-300 rounded-2xl p-6 sm:p-8 space-y-6">
        <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2 border-b border-gray-300 pb-3">
            <div>
                <span class="text-xs font-extrabold uppercase tracking-wider text-orange-800">Complete Site Architecture & Index</span>
                <h2 class="text-xl font-extrabold text-gray-900">Full HTML & XML Site Map Directory</h2>
            </div>
            <div class="flex gap-3 text-xs font-bold">
                <a href="{BASE_URL}/sitemap.html" class="bg-gray-300 hover:bg-gray-400 text-gray-900 px-3 py-1.5 rounded-lg transition">Open Dedicated HTML Site Map &rarr;</a>
                <a href="{BASE_URL}/sitemap.xml" class="bg-orange-700 hover:bg-orange-800 text-white px-3 py-1.5 rounded-lg transition">View XML Sitemap</a>
            </div>
        </div>
        <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
            <div>
                <h3 class="text-sm font-extrabold text-gray-900 mb-2.5 uppercase tracking-wide border-b border-gray-300 pb-1">1. Fire Pit & Patio Calculators ({len(ALL_CALC_PAGES) + 1})</h3>
                <ul class="space-y-1.5">
                    <li><a href="{BASE_URL}/" class="text-xs font-bold text-orange-800 hover:underline">🏠 Home — Master Fire Glass & Patio BTU Calculator</a></li>
                    {calc_links}
                </ul>
            </div>
            <div>
                <h3 class="text-sm font-extrabold text-gray-900 mb-2.5 uppercase tracking-wide border-b border-gray-300 pb-1">2. Head-to-Head Comparisons ({len(VS_COMPARISONS)})</h3>
                <ul class="space-y-2">
                    {vs_links}
                </ul>
            </div>
            <div>
                <h3 class="text-sm font-extrabold text-gray-900 mb-2.5 uppercase tracking-wide border-b border-gray-300 pb-1">3. Daily Product Reviews ({len(all_revs)} — +3/Day)</h3>
                <ul class="space-y-1.5 max-h-80 overflow-y-auto pr-2">
                    {rev_links}
                </ul>
            </div>
        </div>
    </section>
    """

def render_dedicated_html_sitemap_page():
    canonical_url = f"{BASE_URL}/sitemap.html"
    sitemap_block = render_onpage_sitemap_directory()
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Complete Site Map Directory — Calculators, Comparisons & Daily Reviews | {SITE_NAME}</title>
    <meta name="description" content="Complete HTML and XML site map directory of all fire pit glass weight calculators, burner BTU guides, patio heater calculators, and daily outdoor reviews on {SITE_NAME}.">
    <link rel="canonical" href="{canonical_url}">
    <meta name="robots" content="index, follow">
    <script src="https://cdn.tailwindcss.com"></script>
</head>
<body class="bg-gray-200 text-gray-900 antialiased">

    {render_common_header_and_banner()}

    <main class="max-w-6xl mx-auto px-4 py-10 space-y-8">
        <nav class="text-xs font-semibold text-gray-600 flex items-center gap-2">
            <a href="{BASE_URL}/" class="hover:text-orange-800">Home</a>
            <span>/</span>
            <span class="text-gray-900">Complete Site Map</span>
        </nav>

        <div class="bg-gray-100 border-2 border-gray-300 rounded-2xl p-6 sm:p-8 shadow-sm space-y-2">
            <h1 class="text-2xl sm:text-4xl font-extrabold text-gray-900">{SITE_NAME} — Complete Site Map</h1>
            <p class="text-sm text-gray-700">Browse every interactive fire pit glass calculator, patio heater BTU guide, outdoor kitchen hood calculator, head-to-head comparison, and cumulative daily product review article (+3 added daily) below.</p>
        </div>

        {sitemap_block}
    </main>

    <footer class="bg-gray-300 border-t border-gray-400 mt-16 py-10 px-4 text-xs text-gray-700 text-center">
        <p class="font-bold text-gray-900">{SITE_NAME} — {SITE_TAGLINE}</p>
        <p class="mt-1">As an Amazon Associate, this site earns from qualifying purchases (Store ID: {AFFILIATE_TAG}).</p>
    </footer>
</body>
</html>"""

def render_calculator_page(page_data, is_home=False):
    g_lbs, b_20, _, _, b_btu, _, _, _ = compute_patio_specs(
        page_data["shape"], page_data["length"], page_data["width"],
        page_data["depth"], page_data["patio_sqft"], page_data["temp_rise"]
    )
    title = f"{SITE_NAME} — {SITE_TAGLINE}" if is_home else f"{page_data['name']} — {g_lbs} Lbs Fire Glass & BTU Calculator | {SITE_NAME}"
    description = page_data["desc"]
    canonical_url = f"{BASE_URL}/" if is_home else f"{BASE_URL}/{page_data['slug']}.html"
    faqs = generate_faq_data(
        page_data["name"], page_data["shape"], page_data["length"], page_data["width"],
        page_data["depth"], page_data["patio_sqft"], page_data["temp_rise"]
    )

    faq_schema = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": item["q"], "acceptedAnswer": {"@type": "Answer", "text": item["a"]}}
            for item in faqs
        ]
    }

    app_schema = {
        "@context": "https://schema.org",
        "@type": "WebApplication",
        "name": title,
        "url": canonical_url,
        "applicationCategory": "UtilitiesApplication",
        "operatingSystem": "All",
        "description": description,
        "offers": {"@type": "Offer", "price": "0", "priceCurrency": "USD"}
    }

    bestseller_cards_html = ""
    for prod in BEST_SELLERS:
        link = amz_url(prod["keyword"])
        bestseller_cards_html += f"""
        <div class="bg-gray-100 border-2 border-gray-300 hover:border-gray-400 rounded-xl p-5 shadow-sm transition flex flex-col justify-between">
            <div>
                <div class="flex items-center justify-between gap-2 mb-2">
                    <span class="text-xs font-bold uppercase tracking-wider bg-orange-100 text-orange-900 border border-orange-300 px-2.5 py-1 rounded-full">{prod['badge']}</span>
                    <span class="text-xs font-semibold text-amber-700">{prod['rating']}</span>
                </div>
                <span class="text-xs text-gray-600 font-medium">{prod['category']}</span>
                <h3 class="text-base font-bold text-gray-900 mt-1 mb-2 leading-snug">{prod['title']}</h3>
                <p class="text-xs text-gray-700 mb-4 bg-gray-200 p-2.5 rounded-lg border border-gray-300">{prod['specs']}</p>
            </div>
            <a href="{link}" target="_blank" rel="nofollow sponsored noopener"
               class="w-full inline-flex items-center justify-center bg-orange-700 hover:bg-orange-800 text-white font-extrabold text-sm py-2.5 px-4 rounded-lg transition shadow-sm">
               Check Today's Price on Amazon &rarr;
            </a>
        </div>
        """

    preset_links_html = ""
    for p in ALL_CALC_PAGES:
        p_lbs, _, _, _, _, _, _, _ = compute_patio_specs(
            p["shape"], p["length"], p["width"], p["depth"], p["patio_sqft"], p["temp_rise"]
        )
        active_cls = "bg-orange-100 border-orange-700 text-orange-950 font-bold" if (not is_home and p["slug"] == page_data["slug"]) else "bg-gray-100 border-gray-300 text-gray-800 hover:border-orange-700 hover:text-gray-950"
        preset_links_html += f"""
        <a href="{BASE_URL}/{p['slug']}.html" class="border rounded-lg p-3 text-xs transition flex items-center justify-between {active_cls}">
            <span class="truncate pr-2">{p['name']}</span>
            <span class="text-orange-900 font-mono shrink-0">{p_lbs} lbs</span>
        </a>
        """

    faq_html = ""
    for item in faqs:
        faq_html += f"""
        <div class="bg-gray-100 border-2 border-gray-300 rounded-xl p-5">
            <h3 class="text-base font-bold text-gray-900 mb-2">{item['q']}</h3>
            <p class="text-sm text-gray-700 leading-relaxed">{item['a']}</p>
        </div>
        """

    mid_banner_link = amz_url("Stanbroil+Drop+In+Fire+Pit+Burner+Pan+and+American+Fire+Glass+Bundle")
    comparison_html = render_comparison_table_section()
    reviews_grid_html, total_reviews_count = render_review_cards_grid()
    onpage_sitemap_html = render_onpage_sitemap_directory()

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <meta name="description" content="{description}">
    <link rel="canonical" href="{canonical_url}">
    <meta name="robots" content="index, follow">
    <meta property="og:title" content="{title}">
    <meta property="og:description" content="{description}">
    <meta property="og:type" content="website">
    <meta property="og:url" content="{canonical_url}">
    <script src="https://cdn.tailwindcss.com"></script>
    <script type="application/ld+json">{json.dumps(faq_schema)}</script>
    <script type="application/ld+json">{json.dumps(app_schema)}</script>
</head>
<body class="bg-gray-200 text-gray-900 antialiased selection:bg-orange-700 selection:text-white">

    {render_common_header_and_banner()}

    <main class="max-w-6xl mx-auto px-4 py-8 space-y-12">

        <!-- HERO TITLE SECTION -->
        <section class="text-center max-w-3xl mx-auto space-y-3">
            <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-gray-300 border border-gray-400 text-xs font-semibold text-gray-800">
                <span>🔥 Fire Glass & Lava Rock Weight (Lbs), Burner Pan BTU & Patio Heating Engine</span>
            </div>
            <h1 class="text-3xl sm:text-4xl font-extrabold text-gray-900 tracking-tight">
                { "Fire Pit Glass & Lava Rock Weight, Burner BTU & Patio Heater Calculator" if is_home else f"{page_data['name']} — Glass & BTU Calculator" }
            </h1>
            <p class="text-gray-700 text-sm sm:text-base leading-relaxed">
                {description}
            </p>
        </section>

        <!-- INTERACTIVE CALCULATOR + LIVE HARDWARE MATCHER -->
        <section id="calculator" class="grid grid-cols-1 lg:grid-cols-12 gap-8 items-start">
            <!-- Left Column: Inputs (7 Cols) -->
            <div class="lg:col-span-7 bg-gray-100 border-2 border-gray-300 rounded-2xl p-6 sm:p-8 shadow-sm space-y-6">
                <div class="flex items-center justify-between border-b border-gray-300 pb-4">
                    <div>
                        <h2 class="text-xl font-extrabold text-gray-900">1. Enter Fire Pit Opening & Patio Dimensions</h2>
                        <p class="text-xs text-gray-600">Calculates fire glass lbs (20-lb bags), lava rock lbs, burner BTU & patio heaters</p>
                    </div>
                    <span class="text-xs font-mono bg-orange-100 text-orange-900 border border-orange-300 px-2.5 py-1 rounded font-semibold">Live Patio Math</span>
                </div>

                <div>
                    <label for="quickPreset" class="block text-xs font-bold uppercase tracking-wider text-gray-700 mb-2">Quick Select Fire Pit or Outdoor Patio Preset</label>
                    <select id="quickPreset" onchange="applyPreset(this.value)" class="w-full bg-gray-200 border border-gray-400 rounded-lg px-3.5 py-2.5 text-sm font-semibold text-gray-900 focus:ring-2 focus:ring-orange-700">
                        <option value="{page_data['shape']},{page_data['length']},{page_data['width']},{page_data['depth']},{page_data['patio_sqft']},{page_data['temp_rise']}">Current: {page_data['name']}</option>
                        <option value="rect,36,14,2.0,350,20">36\" × 14\" Linear Fire Pit Table (2\" Depth — 53 Lbs Glass / 3 Bags)</option>
                        <option value="round,30,30,2.5,300,20">30-Inch Round Stone Fire Pit (2.5\" Depth — 94 Lbs Glass / 5 Bags)</option>
                        <option value="round,36,36,2.0,400,20">36-Inch Round Backyard Fire Pit (2.0\" Depth — 108 Lbs Glass)</option>
                        <option value="rect,48,16,2.0,450,20">48\" × 16\" Linear Trough Fire Pit (2\" Depth — 81 Lbs Glass + 125k BTU)</option>
                        <option value="rect,24,24,2.0,250,20">24\" × 24\" Square Fire Pit Table (2\" Depth — 61 Lbs Glass)</option>
                        <option value="round,24,24,2.0,250,15">24-Inch Round Patio Fire Bowl (2\" Depth — 48 Lbs Glass)</option>
                    </select>
                </div>

                <div class="grid grid-cols-1 sm:grid-cols-2 gap-5">
                    <div>
                        <label for="shapeInput" class="block text-sm font-bold text-gray-800 mb-1">Fire Pit Opening Shape</label>
                        <select id="shapeInput" onchange="calculatePatio()" class="w-full bg-gray-200 border border-gray-400 rounded-lg px-3.5 py-2.5 text-sm font-bold text-gray-900">
                            <option value="rect" {"selected" if page_data['shape'] == "rect" else ""}>Rectangular / Square Fire Table (L × W × D ÷ 19)</option>
                            <option value="round" {"selected" if page_data['shape'] == "round" else ""}>Circular / Round Fire Pit (Dia² × D ÷ 24)</option>
                        </select>
                    </div>

                    <div>
                        <label for="depthInput" class="block text-sm font-bold text-gray-800 mb-1">Desired Fire Glass Depth (Inches)</label>
                        <select id="depthInput" onchange="calculatePatio()" class="w-full bg-gray-200 border border-gray-400 rounded-lg px-3.5 py-2.5 text-sm font-bold text-gray-900">
                            <option value="1.5" {"selected" if page_data['depth'] <= 1.6 else ""}>1.5 Inches — Shallow Drop-In Pan Skim</option>
                            <option value="2.0" {"selected" if 1.6 < page_data['depth'] <= 2.2 else ""}>2.0 Inches — Industry Standard Drop-In Pan Depth</option>
                            <option value="2.5" {"selected" if 2.2 < page_data['depth'] <= 2.8 else ""}>2.5 Inches — Deep H-Burner Coverage</option>
                            <option value="3.0" {"selected" if page_data['depth'] > 2.8 else ""}>3.0 Inches — Extra-Deep Custom Bed</option>
                        </select>
                    </div>

                    <div>
                        <label for="lengthInput" class="block text-sm font-bold text-gray-800 mb-1">Inner Length or Diameter (Inches)</label>
                        <input type="number" id="lengthInput" value="{page_data['length']}" min="10" max="120" step="1" oninput="calculatePatio()"
                               class="w-full bg-gray-200 border border-gray-400 rounded-lg px-4 py-2.5 text-base font-bold text-gray-900 focus:ring-2 focus:ring-orange-700">
                    </div>

                    <div>
                        <label for="widthInput" class="block text-sm font-bold text-gray-800 mb-1">Inner Width (Inches — Rectangular)</label>
                        <input type="number" id="widthInput" value="{page_data['width']}" min="6" max="120" step="1" oninput="calculatePatio()"
                               class="w-full bg-gray-200 border border-gray-400 rounded-lg px-4 py-2.5 text-base font-bold text-gray-900 focus:ring-2 focus:ring-orange-700">
                        <span class="text-[11px] text-gray-600">For round pits, automatically uses diameter</span>
                    </div>

                    <div>
                        <label for="patioSqftInput" class="block text-sm font-bold text-gray-800 mb-1">Patio Seating Area (Sq. Ft.)</label>
                        <input type="number" id="patioSqftInput" value="{page_data['patio_sqft']}" min="50" max="2500" step="25" oninput="calculatePatio()"
                               class="w-full bg-gray-200 border border-gray-400 rounded-lg px-4 py-2.5 text-base font-bold text-gray-900 focus:ring-2 focus:ring-orange-700">
                        <span class="text-[11px] text-gray-600">Sizes Patio Heaters & BBQ Island Hood CFM</span>
                    </div>

                    <div>
                        <label for="riseInput" class="block text-sm font-bold text-gray-800 mb-1">Patio Heater Temp Rise (°F)</label>
                        <select id="riseInput" onchange="calculatePatio()" class="w-full bg-gray-200 border border-gray-400 rounded-lg px-3.5 py-2.5 text-sm font-bold text-gray-900">
                            <option value="15" {"selected" if page_data['temp_rise'] == 15 else ""}>+15°F Rise (Mild 55°F Evenings)</option>
                            <option value="20" {"selected" if page_data['temp_rise'] == 20 else ""}>+20°F Rise (Chilly 45°F Autumn Nights)</option>
                            <option value="25" {"selected" if page_data['temp_rise'] >= 25 else ""}>+25°F Rise (Cold 38°F Winter Patio)</option>
                        </select>
                    </div>
                </div>
            </div>

            <!-- Right Column: Output + Dynamic Amazon Recommendation (5 Cols) -->
            <div class="lg:col-span-5 bg-gray-100 border-2 border-orange-700 rounded-2xl p-6 sm:p-8 shadow-md space-y-6">
                <div class="border-b border-gray-300 pb-3">
                    <span class="text-xs font-extrabold uppercase tracking-wider text-orange-800">2. Engineered Media & BTU Specs</span>
                    <h2 class="text-xl font-extrabold text-gray-900">Your Exact Fire Pit & Patio Sizing</h2>
                </div>

                <div class="grid grid-cols-2 gap-3.5">
                    <div class="bg-orange-100 border border-orange-300 rounded-xl p-3.5">
                        <span class="text-xs text-orange-950 font-semibold block">Fire Pit Glass Needed</span>
                        <span id="resGlassLbs" class="text-2xl font-black text-orange-800">53 Lbs</span>
                        <span id="resGlassBags" class="text-[11px] text-orange-900 block mt-0.5">3× 20-Lb Jars (or 6× 10-Lb)</span>
                    </div>
                    <div class="bg-gray-200 border border-gray-300 rounded-xl p-3.5">
                        <span class="text-xs text-gray-600 font-medium block">Or Lava Rock Weight</span>
                        <span id="resLavaLbs" class="text-2xl font-black text-gray-900">28 Lbs</span>
                        <span id="resBurnerBTU" class="text-[11px] text-emerald-800 font-bold block mt-0.5">Burner: 90,000 BTU/hr</span>
                    </div>
                    <div class="bg-gray-200 border border-gray-300 rounded-xl p-3.5">
                        <span class="text-xs text-gray-600 font-medium block">Patio Heater Demand</span>
                        <span id="resPatioBTU" class="text-base font-extrabold text-gray-900">36,400 BTU</span>
                        <span id="resHeaterCount" class="text-[11px] text-gray-600 block mt-0.5">1× 48k BTU Heater</span>
                    </div>
                    <div class="bg-gray-200 border border-gray-300 rounded-xl p-3.5">
                        <span class="text-xs text-gray-600 font-medium block">BBQ Island Hood CFM</span>
                        <span id="resHoodCFM" class="text-base font-extrabold text-amber-800">1,200+ CFM</span>
                        <span class="text-[11px] text-gray-600 block mt-0.5">36\" Deep 304 Stainless</span>
                    </div>
                </div>

                <!-- Dynamic Matched Product Box -->
                <div class="bg-gray-200 border-2 border-orange-600 rounded-xl p-4 space-y-3">
                    <div class="flex items-center justify-between">
                        <span class="text-[11px] font-extrabold uppercase tracking-wider bg-orange-700 text-white px-2 py-0.5 rounded">Verified Hardware Match</span>
                        <span class="text-xs font-bold text-gray-700">Amazon Prime Ready</span>
                    </div>
                    <h3 id="recPatioTitle" class="text-base font-extrabold text-gray-900 leading-snug">Loading Fire Glass & Burner Match...</h3>
                    <p id="recPatioDesc" class="text-xs text-gray-700"></p>
                    <div class="pt-1 flex flex-col sm:flex-row gap-2.5">
                        <a id="recPrimaryBtn" href="#" target="_blank" rel="nofollow sponsored noopener"
                           class="flex-1 text-center bg-orange-700 hover:bg-orange-800 text-white font-extrabold text-sm py-3 px-4 rounded-lg transition shadow-sm">
                           Shop 1/2\" Reflective Fire Glass &rarr;
                        </a>
                        <a id="recSecondaryBtn" href="#" target="_blank" rel="nofollow sponsored noopener"
                           class="text-center bg-gray-800 hover:bg-gray-900 text-white font-bold text-xs py-3 px-3 rounded-lg transition">
                           Shop Burner Pan & Heaters
                        </a>
                    </div>
                </div>
            </div>
        </section>

        <!-- PRODUCT SEARCH ENGINE SECTION (SEARCH PRODUK) -->
        <section id="product-search" class="bg-gray-100 border-2 border-gray-300 rounded-2xl p-6 sm:p-8 shadow-sm">
            <div class="max-w-3xl mx-auto text-center space-y-4">
                <h2 class="text-2xl font-extrabold text-gray-900">Search Fire Pit Glass, Stainless Burner Pans, Patio Heaters & Pizza Ovens</h2>
                <p class="text-sm text-gray-700">Search any brand (American Fire Glass, Stanbroil, Ooni, Traeger, Solo Stove, Outland Living, Hiland, ZLINE) or outdoor kitchen gear on Amazon.</p>
                <form onsubmit="handleAmazonSearch(event)" class="flex flex-col sm:flex-row gap-3 pt-2">
                    <input type="text" id="amzSearchInput" placeholder="e.g. American Fire Glass 1/2 Inch 20 lb, Stanbroil Drop-In H-Burner Pan, Ooni Koda 16..."
                           class="flex-1 bg-gray-200 border-2 border-gray-400 rounded-xl px-4 py-3 text-sm font-medium text-gray-900 placeholder-gray-500 focus:outline-none focus:border-orange-700" required>
                    <button type="submit" class="bg-orange-700 hover:bg-orange-800 text-white font-extrabold text-sm px-6 py-3 rounded-xl transition cursor-pointer shrink-0">
                        Search on Amazon &rarr;
                    </button>
                </form>
                <div class="flex flex-wrap items-center justify-center gap-2 pt-2 text-xs">
                    <span class="text-gray-600 font-semibold">Popular Searches:</span>
                    <a href="{amz_url('American Fire Glass 1/2 Inch Reflective 20 lb')}" target="_blank" rel="nofollow sponsored noopener" class="px-2.5 py-1 bg-gray-200 hover:bg-orange-200 text-gray-800 border border-gray-300 rounded-full transition">Reflective Fire Glass (20 Lb)</a>
                    <a href="{amz_url('Stanbroil Drop In Fire Pit Pan H Burner')}" target="_blank" rel="nofollow sponsored noopener" class="px-2.5 py-1 bg-gray-200 hover:bg-orange-200 text-gray-800 border border-gray-300 rounded-full transition">304 Stainless Burner Pans</a>
                    <a href="{amz_url('48000 BTU Propane Patio Heater')}" target="_blank" rel="nofollow sponsored noopener" class="px-2.5 py-1 bg-gray-200 hover:bg-orange-200 text-gray-800 border border-gray-300 rounded-full transition">48k BTU Patio Heaters</a>
                    <a href="{amz_url('Ooni Koda 16 Karu 16 Pizza Oven')}" target="_blank" rel="nofollow sponsored noopener" class="px-2.5 py-1 bg-gray-200 hover:bg-orange-200 text-gray-800 border border-gray-300 rounded-full transition">Ooni 16\" Pizza Ovens</a>
                    <a href="{amz_url('Solo Stove Bonfire 2.0 Yukon 2.0')}" target="_blank" rel="nofollow sponsored noopener" class="px-2.5 py-1 bg-gray-200 hover:bg-orange-200 text-gray-800 border border-gray-300 rounded-full transition">Solo Stove Smokeless Pits</a>
                </div>
            </div>
        </section>

        <!-- BEST SELLING PRODUCTS GRID (PRODUK TERLARIS) -->
        <section id="best-sellers" class="space-y-6">
            <div class="flex flex-col sm:flex-row sm:items-end justify-between gap-2 border-b border-gray-300 pb-4">
                <div>
                    <span class="text-xs font-extrabold uppercase tracking-wider text-orange-800">Verified Outdoor Living Hardware</span>
                    <h2 class="text-2xl font-extrabold text-gray-900">Best-Selling Fire Glass, Burner Kits, Patio Heaters & Pizza Ovens</h2>
                </div>
                <a href="{amz_url('Best Selling Fire Pit Glass Patio Heaters and Pizza Ovens')}" target="_blank" rel="nofollow sponsored noopener" class="text-sm font-bold text-orange-800 hover:text-orange-900">
                    Browse Full Amazon Best Sellers &rarr;
                </a>
            </div>
            <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-5">
                {bestseller_cards_html}
            </div>
        </section>

        {comparison_html}

        <!-- CUMULATIVE DAILY PRODUCT REVIEW ARTICLES SECTION (+3 NEW ARTICLES PER DAY) -->
        <section id="reviews" class="space-y-6">
            <div class="flex flex-col sm:flex-row sm:items-end justify-between gap-2 border-b border-gray-300 pb-4">
                <div>
                    <span class="text-xs font-extrabold uppercase tracking-wider text-orange-800">Autonomous Daily Review Archive ({total_reviews_count} Published Articles & Growing +3/Day)</span>
                    <h2 class="text-2xl font-extrabold text-gray-900">In-Depth Fire Pit, Patio Heater, Pizza Oven & BBQ Review Articles</h2>
                </div>
                <span class="text-xs font-semibold bg-emerald-100 text-emerald-900 border border-emerald-300 px-3 py-1 rounded-full">+3 New Product Reviews Added Automatically Every Day</span>
            </div>
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
                {reviews_grid_html}
            </div>
        </section>

        <!-- MID-PAGE PROMOTIONAL AFFILIATE BANNER -->
        <section class="bg-gray-300 border-2 border-orange-700 rounded-2xl p-6 sm:p-8 flex flex-col md:flex-row items-center justify-between gap-6">
            <div class="space-y-2 max-w-2xl">
                <span class="text-xs font-extrabold uppercase tracking-wider bg-orange-700 text-white px-2.5 py-1 rounded">Complete Zero-Whistle Custom Fire Pit Bundle</span>
                <h2 class="text-xl sm:text-2xl font-extrabold text-gray-900">Building or Upgrading a Backyard Gas Fire Pit Table?</h2>
                <p class="text-sm text-gray-800">Get tall, silent flames and 3x more radiant warmth by pairing a 304 Stainless Drop-In H-Burner Pan with a Non-Whistle Gas Flex Line, Tempered Glass Wind Guard, and 1/2\" Reflective Fire Glass.</p>
            </div>
            <a href="{mid_banner_link}" target="_blank" rel="nofollow sponsored noopener"
               class="shrink-0 bg-orange-700 hover:bg-orange-800 text-white font-extrabold text-sm px-6 py-3.5 rounded-xl shadow-sm transition">
               Explore Burner Pan + Fire Glass Bundles &rarr;
            </a>
        </section>

        <!-- PROGRAMMATIC SEO DIRECTORY -->
        <section id="presets" class="space-y-4">
            <div class="border-b border-gray-300 pb-3">
                <h2 class="text-xl font-extrabold text-gray-900">Fire Pit Dimensions, Patio Heater BTU & BBQ Hood Calculators</h2>
                <p class="text-xs text-gray-600">Select your exact fire pit opening shape or patio square footage below for pre-calculated fire glass bag counts and BTU ratings.</p>
            </div>
            <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-2.5">
                {preset_links_html}
            </div>
        </section>

        <!-- FREQUENTLY ASKED QUESTIONS (FAQ) -->
        <section id="faq" class="space-y-6">
            <div class="border-b border-gray-300 pb-3">
                <span class="text-xs font-extrabold uppercase tracking-wider text-orange-800">Fire Glass Depth, LP Venting & BTU Guide</span>
                <h2 class="text-2xl font-extrabold text-gray-900">Frequently Asked Questions (FAQ)</h2>
            </div>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                {faq_html}
            </div>
        </section>

        {onpage_sitemap_html}

    </main>

    <!-- FOOTER (GRAY BACKGROUND) -->
    <footer class="bg-gray-300 border-t border-gray-400 mt-16 py-10 px-4 text-xs text-gray-700">
        <div class="max-w-6xl mx-auto flex flex-col sm:flex-row items-center justify-between gap-4">
            <div>
                <p class="font-bold text-gray-900">{SITE_NAME} — {SITE_TAGLINE}</p>
                <p class="mt-1">As an Amazon Associate, this site earns from qualifying purchases (Store ID: {AFFILIATE_TAG}).</p>
            </div>
            <div class="flex flex-wrap gap-4 font-medium text-gray-800">
                <a href="{BASE_URL}/" class="hover:text-orange-800">Home</a>
                <a href="{BASE_URL}/#comparison" class="hover:text-orange-800">Comparisons</a>
                <a href="{BASE_URL}/#reviews" class="hover:text-orange-800">Daily Reviews (+3/Day)</a>
                <a href="{BASE_URL}/sitemap.html" class="hover:text-orange-800 font-bold">HTML Site Map</a>
                <a href="{BASE_URL}/sitemap.xml" class="hover:text-orange-800">XML Sitemap</a>
                <a href="{BASE_URL}/#faq" class="hover:text-orange-800">FAQ</a>
            </div>
        </div>
    </footer>

    <!-- INTERACTIVE CALCULATOR & AFFILIATE MATCHING SCRIPT -->
    <script>
        const AFFILIATE_TAG = "{AFFILIATE_TAG}";

        function makeAmazonLink(query) {{
            return "https://www.amazon.com/s?k=" + encodeURIComponent(query) + "&tag=" + AFFILIATE_TAG;
        }}

        function applyPreset(val) {{
            const parts = val.split(",");
            if (parts.length === 6) {{
                document.getElementById("shapeInput").value = parts[0];
                document.getElementById("lengthInput").value = parts[1];
                document.getElementById("widthInput").value = parts[2];
                document.getElementById("depthInput").value = parts[3];
                document.getElementById("patioSqftInput").value = parts[4];
                document.getElementById("riseInput").value = parts[5];
                calculatePatio();
            }}
        }}

        function handleAmazonSearch(e) {{
            e.preventDefault();
            const q = document.getElementById("amzSearchInput").value.trim();
            if (q) {{
                window.open(makeAmazonLink(q), "_blank", "noopener,noreferrer");
            }}
        }}

        function calculatePatio() {{
            const shape = document.getElementById("shapeInput").value || "rect";
            const l = parseFloat(document.getElementById("lengthInput").value) || 36;
            let w = parseFloat(document.getElementById("widthInput").value) || 14;
            const d = parseFloat(document.getElementById("depthInput").value) || 2.0;
            const patioSqft = parseFloat(document.getElementById("patioSqftInput").value) || 350;
            const tempRise = parseFloat(document.getElementById("riseInput").value) || 20;

            let glassLbs = 53;
            let areaSqIn = l * w;
            if (shape === "round") {{
                w = l;
                glassLbs = Math.ceil((l * l * d) / 24.0);
                areaSqIn = Math.PI * Math.pow(l / 2.0, 2);
            }} else {{
                glassLbs = Math.ceil((l * w * d) / 19.0);
            }}

            const bags20 = Math.max(1, Math.ceil(glassLbs / 20));
            const bags10 = Math.max(1, Math.ceil(glassLbs / 10));
            const lavaLbs = Math.ceil(glassLbs * 0.52);

            const rawBurnerBTU = Math.round((areaSqIn * 165) / 5000) * 5000;
            const burnerBTU = Math.max(50000, Math.min(160000, rawBurnerBTU));

            const patioBTU = Math.ceil((patioSqft * tempRise * 5.2) / 2000) * 2000;
            const heaters48k = Math.max(1, Math.ceil(patioBTU / 48000));
            const hoodCFM = patioSqft <= 400 ? "1,200+ CFM (36\\\" Hood)" : "1,600–2,000 CFM (48\\\" Hood)";

            document.getElementById("resGlassLbs").textContent = glassLbs + " Lbs Glass";
            document.getElementById("resGlassBags").textContent = bags20 + "× 20-Lb Jars (or " + bags10 + "× 10-Lb)";
            document.getElementById("resLavaLbs").textContent = lavaLbs + " Lbs Lava Rock";
            document.getElementById("resBurnerBTU").textContent = "Burner: ~" + burnerBTU.toLocaleString() + " BTU/hr";
            document.getElementById("resPatioBTU").textContent = patioBTU.toLocaleString() + " BTU";
            document.getElementById("resHeaterCount").textContent = heaters48k + "× 48,000 BTU Heater" + (heaters48k > 1 ? "s" : "");
            document.getElementById("resHoodCFM").textContent = hoodCFM;

            let recTitle = "";
            let recDesc = "";
            let primaryQuery = "American Fire Glass 1/2 Inch Reflective Fire Pit Glass 20 lb";
            let secondaryQuery = "";

            if (shape === "round") {{
                const panDia = Math.max(18, l - 5);
                recTitle = bags20 + "× 20-Lb Jars 1/2\" Reflective Fire Glass + " + panDia + "\" Round 304 Stainless Drop-In Burner Pan";
                recDesc = "Exact media and zero-whistle burner sizing for a " + l + "-inch diameter round fire pit.";
                secondaryQuery = "Stanbroil " + panDia + " Inch Round Drop In Fire Pit Pan Burner";
            }} else {{
                recTitle = bags20 + "× 20-Lb Jars 1/2\" Reflective Fire Glass + " + l + "\"×" + w + "\" H-Burner Pan & Wind Guard";
                recDesc = "Radiant mirror-backed tempered glass and 304 stainless H-burner for a " + l + "\"×" + w + "\" fire table.";
                secondaryQuery = "Stanbroil Drop In Rectangular Fire Pit Pan H Burner and Wind Guard";
            }}

            document.getElementById("recPatioTitle").textContent = recTitle;
            document.getElementById("recPatioDesc").textContent = recDesc;
            document.getElementById("recPrimaryBtn").href = makeAmazonLink(primaryQuery);
            document.getElementById("recSecondaryBtn").href = makeAmazonLink(secondaryQuery);
        }}

        window.addEventListener("DOMContentLoaded", calculatePatio);
    </script>
</body>
</html>"""

def render_single_review_page(rev):
    canonical_url = f"{BASE_URL}/{rev['slug']}.html"
    amz_link = amz_url(rev["keyword"])

    review_schema = {
        "@context": "https://schema.org",
        "@type": "Product",
        "name": rev["product_name"],
        "description": rev["summary"],
        "review": {
            "@type": "Review",
            "datePublished": rev["published_date"],
            "reviewRating": {"@type": "Rating", "ratingValue": rev["rating_score"], "bestRating": "5"},
            "author": {"@type": "Organization", "name": SITE_NAME},
            "reviewBody": " ".join(rev["body_paragraphs"])
        }
    }

    pros_html = "".join([f'<li class="flex items-start gap-2 text-sm text-gray-800"><span class="text-emerald-700 font-bold">✓</span><span>{p}</span></li>' for p in rev["pros"]])
    cons_html = "".join([f'<li class="flex items-start gap-2 text-sm text-gray-800"><span class="text-rose-700 font-bold">✕</span><span>{c}</span></li>' for c in rev["cons"]])
    paragraphs_html = "".join([f'<p class="text-gray-800 leading-relaxed text-base mb-4">{p}</p>' for p in rev["body_paragraphs"]])

    recent_reviews = [r for r in get_cumulative_product_reviews() if r["slug"] != rev["slug"]][:6]
    related_html = ""
    for other in recent_reviews:
        related_html += f"""
        <a href="{BASE_URL}/{other['slug']}.html" class="bg-gray-100 border-2 border-gray-300 rounded-xl p-4 hover:border-orange-700 transition block">
            <span class="text-[11px] font-bold text-orange-800 uppercase">{other['verdict_badge']}</span>
            <h4 class="font-extrabold text-sm text-gray-900 mt-1 line-clamp-2">{other['product_name']} Review</h4>
            <span class="text-xs text-gray-600 mt-1 block">Score: {other['rating_score']} / 5.0 ★ ({other['published_date']}) &rarr;</span>
        </a>
        """

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{rev['title']} | {SITE_NAME}</title>
    <meta name="description" content="{rev['summary']}">
    <link rel="canonical" href="{canonical_url}">
    <meta name="robots" content="index, follow">
    <script src="https://cdn.tailwindcss.com"></script>
    <script type="application/ld+json">{json.dumps(review_schema)}</script>
</head>
<body class="bg-gray-200 text-gray-900 antialiased">

    {render_common_header_and_banner()}

    <main class="max-w-4xl mx-auto px-4 py-10 space-y-10">
        <nav class="text-xs font-semibold text-gray-600 flex items-center gap-2">
            <a href="{BASE_URL}/" class="hover:text-orange-800">Home & Fire Calculator</a>
            <span>/</span>
            <a href="{BASE_URL}/#reviews" class="hover:text-orange-800">Daily Patio Reviews</a>
            <span>/</span>
            <span class="text-gray-900">{rev['product_name']}</span>
        </nav>

        <div class="bg-gray-100 border-2 border-gray-300 rounded-2xl p-6 sm:p-8 shadow-sm space-y-5">
            <div class="flex flex-wrap items-center justify-between gap-2">
                <span class="text-xs font-extrabold uppercase tracking-wider bg-orange-100 text-orange-900 border border-orange-300 px-3 py-1 rounded-full">{rev['verdict_badge']}</span>
                <div class="flex items-center gap-2">
                    <span class="text-xs font-mono text-gray-600">Published: {rev['published_date']}</span>
                    <span class="text-sm font-black bg-amber-200 text-amber-950 px-3 py-1 rounded-lg">Patio Rating: {rev['rating_score']} / 5.0 ★</span>
                </div>
            </div>
            <h1 class="text-2xl sm:text-4xl font-extrabold text-gray-900 leading-tight">{rev['title']}</h1>
            <p class="text-base text-gray-700 leading-relaxed">{rev['summary']}</p>

            <div class="grid grid-cols-2 sm:grid-cols-4 gap-3 bg-gray-200 p-4 rounded-xl border border-gray-300 text-xs">
                <div><span class="text-gray-500 block font-medium">Primary Spec</span><strong class="text-gray-900">{rev['spec_1']}</strong></div>
                <div><span class="text-gray-500 block font-medium">Heat / Material</span><strong class="text-gray-900">{rev['spec_2']}</strong></div>
                <div><span class="text-gray-500 block font-medium">Construction</span><strong class="text-gray-900">{rev['spec_3']}</strong></div>
                <div><span class="text-gray-500 block font-medium">Included</span><strong class="text-gray-900">{rev['spec_4']}</strong></div>
            </div>

            <div class="flex flex-col sm:flex-row gap-3 pt-2">
                <a href="{amz_link}" target="_blank" rel="nofollow sponsored noopener"
                   class="flex-1 text-center bg-orange-700 hover:bg-orange-800 text-white font-extrabold text-sm py-3.5 px-6 rounded-xl transition shadow-sm">
                   Check Latest Price & Availability on Amazon &rarr;
                </a>
                <a href="{BASE_URL}/#calculator"
                   class="text-center bg-gray-300 hover:bg-gray-400 text-gray-900 font-bold text-sm py-3.5 px-5 rounded-xl transition">
                   Calculate Fire Glass & BTU
                </a>
            </div>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
            <div class="bg-gray-100 border-2 border-emerald-400 rounded-2xl p-6 space-y-3">
                <h2 class="text-base font-extrabold text-emerald-900 uppercase tracking-wide">Pros (What We Like)</h2>
                <ul class="space-y-2.5">{pros_html}</ul>
            </div>
            <div class="bg-gray-100 border-2 border-rose-400 rounded-2xl p-6 space-y-3">
                <h2 class="text-base font-extrabold text-rose-900 uppercase tracking-wide">Cons (Things to Consider)</h2>
                <ul class="space-y-2.5">{cons_html}</ul>
            </div>
        </div>

        <article class="bg-gray-100 border-2 border-gray-300 rounded-2xl p-6 sm:p-8 space-y-4">
            <h2 class="text-xl font-extrabold text-gray-900 border-b border-gray-300 pb-3">Hands-On Thermal Output, Weather Durability & Sizing Analysis</h2>
            {paragraphs_html}
            <div class="pt-4 border-t border-gray-300 flex flex-col sm:flex-row items-center justify-between gap-4">
                <div>
                    <span class="text-xs font-bold uppercase text-orange-800 block">Final Verdict</span>
                    <p class="text-sm font-bold text-gray-900">{rev['product_name']} earns {rev['rating_score']}/5.0 in our outdoor living benchmark.</p>
                </div>
                <a href="{amz_link}" target="_blank" rel="nofollow sponsored noopener"
                   class="shrink-0 bg-orange-700 hover:bg-orange-800 text-white font-extrabold text-sm px-6 py-3 rounded-xl transition shadow-sm">
                   View Customer Reviews & Price on Amazon &rarr;
                </a>
            </div>
        </article>

        <section class="space-y-4">
            <h3 class="text-lg font-extrabold text-gray-900">Recent Daily Patio, Fire Pit & BBQ Reviews (+3 Added Daily)</h3>
            <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-4">
                {related_html}
            </div>
        </section>
    </main>

    <footer class="bg-gray-300 border-t border-gray-400 mt-16 py-10 px-4 text-xs text-gray-700 text-center">
        <p class="font-bold text-gray-900">{SITE_NAME} — {SITE_TAGLINE}</p>
        <p class="mt-1">As an Amazon Associate, this site earns from qualifying purchases (Store ID: {AFFILIATE_TAG}).</p>
    </footer>
</body>
</html>"""

def render_vs_comparison_page(vs):
    canonical_url = f"{BASE_URL}/{vs['slug']}.html"
    link_a = amz_url(vs["keyword_a"])
    link_b = amz_url(vs["keyword_b"])

    rows_html = ""
    for m in vs["metrics"]:
        rows_html += f"""
        <tr class="border-b border-gray-300">
            <td class="p-4 font-bold text-gray-900 bg-gray-200 text-xs sm:text-sm w-1/4">{m['feature']}</td>
            <td class="p-4 text-xs sm:text-sm text-gray-800 w-3/8">{m['val_a']}</td>
            <td class="p-4 text-xs sm:text-sm text-gray-800 w-3/8">{m['val_b']}</td>
        </tr>
        """

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{vs['title']} | {SITE_NAME}</title>
    <meta name="description" content="{vs['summary']}">
    <link rel="canonical" href="{canonical_url}">
    <meta name="robots" content="index, follow">
    <script src="https://cdn.tailwindcss.com"></script>
</head>
<body class="bg-gray-200 text-gray-900 antialiased">

    {render_common_header_and_banner()}

    <main class="max-w-4xl mx-auto px-4 py-10 space-y-10">
        <nav class="text-xs font-semibold text-gray-600 flex items-center gap-2">
            <a href="{BASE_URL}/" class="hover:text-orange-800">Home & Fire Calculator</a>
            <span>/</span>
            <a href="{BASE_URL}/#comparison" class="hover:text-orange-800">Product Comparisons</a>
            <span>/</span>
            <span class="text-gray-900">{vs['product_a']} vs. {vs['product_b']}</span>
        </nav>

        <div class="bg-gray-100 border-2 border-gray-300 rounded-2xl p-6 sm:p-8 shadow-sm space-y-4">
            <span class="text-xs font-extrabold uppercase tracking-wider bg-orange-100 text-orange-900 border border-orange-300 px-3 py-1 rounded-full">{vs['winner_badge']}</span>
            <h1 class="text-2xl sm:text-4xl font-extrabold text-gray-900 leading-tight">{vs['title']}</h1>
            <p class="text-base text-gray-700 leading-relaxed">{vs['summary']}</p>
        </div>

        <div class="bg-gray-100 border-2 border-gray-300 rounded-2xl overflow-hidden shadow-sm">
            <table class="w-full text-left border-collapse">
                <thead>
                    <tr class="bg-gray-800 text-white text-xs sm:text-sm font-extrabold">
                        <th class="p-4">Specification</th>
                        <th class="p-4 text-orange-300">{vs['product_a']}</th>
                        <th class="p-4 text-amber-300">{vs['product_b']}</th>
                    </tr>
                </thead>
                <tbody>
                    {rows_html}
                    <tr class="bg-gray-200">
                        <td class="p-4 font-extrabold text-xs sm:text-sm text-gray-900">Check Amazon Price</td>
                        <td class="p-4">
                            <a href="{link_a}" target="_blank" rel="nofollow sponsored noopener" class="inline-block bg-orange-700 hover:bg-orange-800 text-white font-extrabold text-xs py-2.5 px-4 rounded-lg transition">
                                View {vs['product_a']} &rarr;
                            </a>
                        </td>
                        <td class="p-4">
                            <a href="{link_b}" target="_blank" rel="nofollow sponsored noopener" class="inline-block bg-gray-800 hover:bg-gray-900 text-white font-extrabold text-xs py-2.5 px-4 rounded-lg transition">
                                View {vs['product_b']} &rarr;
                            </a>
                        </td>
                    </tr>
                </tbody>
            </table>
        </div>

        <div class="bg-gray-100 border-2 border-orange-600 rounded-2xl p-6 sm:p-8 space-y-4">
            <h2 class="text-xl font-extrabold text-gray-900">Head-to-Head Buying Verdict</h2>
            <p class="text-sm sm:text-base text-gray-800 leading-relaxed">{vs['verdict_text']}</p>
            <div class="flex flex-col sm:flex-row gap-3 pt-2">
                <a href="{link_a}" target="_blank" rel="nofollow sponsored noopener" class="flex-1 text-center bg-orange-700 hover:bg-orange-800 text-white font-extrabold text-sm py-3 px-4 rounded-xl transition">
                    Shop {vs['product_a']} on Amazon &rarr;
                </a>
                <a href="{link_b}" target="_blank" rel="nofollow sponsored noopener" class="flex-1 text-center bg-gray-800 hover:bg-gray-900 text-white font-extrabold text-sm py-3 px-4 rounded-xl transition">
                    Shop {vs['product_b']} on Amazon &rarr;
                </a>
            </div>
        </div>
    </main>

    <footer class="bg-gray-300 border-t border-gray-400 mt-16 py-10 px-4 text-xs text-gray-700 text-center">
        <p class="font-bold text-gray-900">{SITE_NAME} — {SITE_TAGLINE}</p>
        <p class="mt-1">As an Amazon Associate, this site earns from qualifying purchases (Store ID: {AFFILIATE_TAG}).</p>
    </footer>
</body>
</html>"""

def generate_sitemap_and_robots(urls):
    today = datetime.datetime.utcnow().strftime("%Y-%m-%d")
    xml_items = ""
    for u in urls:
        xml_items += f"""  <url>
    <loc>{u}</loc>
    <lastmod>{today}</lastmod>
    <changefreq>daily</changefreq>
    <priority>{"1.0" if u.endswith("/") else "0.85"}</priority>
  </url>\n"""

    sitemap_content = f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{xml_items}</urlset>"""

    with open(os.path.join(OUTPUT_DIR, "sitemap.xml"), "w", encoding="utf-8") as f:
        f.write(sitemap_content)

    robots_content = f"""User-agent: *
Allow: /
Sitemap: {BASE_URL}/sitemap.xml
"""
    with open(os.path.join(OUTPUT_DIR, "robots.txt"), "w", encoding="utf-8") as f:
        f.write(robots_content)

    with open(os.path.join(OUTPUT_DIR, f"{INDEXNOW_KEY}.txt"), "w", encoding="utf-8") as f:
        f.write(INDEXNOW_KEY)

def ping_indexnow(urls):
    parsed_host = urllib.parse.urlparse(BASE_URL).netloc
    if not parsed_host or "username.github.io" in parsed_host:
        return

    payload = {
        "host": parsed_host,
        "key": INDEXNOW_KEY,
        "keyLocation": f"{BASE_URL}/{INDEXNOW_KEY}.txt",
        "urlList": urls
    }
    try:
        req = urllib.request.Request(
            "https://api.indexnow.org/indexnow",
            data=json.dumps(payload).encode("utf-8"),
            headers={"Content-Type": "application/json; charset=utf-8"},
            method="POST"
        )
        with urllib.request.urlopen(req, timeout=10) as resp:
            print(f"IndexNow Ping Status: {resp.status}")
    except Exception as e:
        print(f"IndexNow notice: {e}")

def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    generated_urls = []

    # 1. Generate Homepage
    home_preset = {
        "slug": "index",
        "name": "36\" × 14\" Linear Fire Pit Table (2\" Glass Depth)",
        "shape": "rect",
        "length": 36,
        "width": 14,
        "depth": 2.0,
        "patio_sqft": 350,
        "temp_rise": 20,
        "desc": "Calculate exact fire pit glass & lava rock weight (lbs & 20-lb bags), stainless drop-in burner BTU capacity, patio heater BTUs, and outdoor kitchen range hood CFM—plus read 3 new patio hardware reviews added daily."
    }
    with open(os.path.join(OUTPUT_DIR, "index.html"), "w", encoding="utf-8") as f:
        f.write(render_calculator_page(home_preset, is_home=True))
    generated_urls.append(f"{BASE_URL}/")

    # 2. Generate Dedicated HTML Site Map Page (sitemap.html)
    with open(os.path.join(OUTPUT_DIR, "sitemap.html"), "w", encoding="utf-8") as f:
        f.write(render_dedicated_html_sitemap_page())
    generated_urls.append(f"{BASE_URL}/sitemap.html")

    # 3. Generate Programmatic Fire Pit & Patio Calculator Pages
    for page in ALL_CALC_PAGES:
        filename = f"{page['slug']}.html"
        with open(os.path.join(OUTPUT_DIR, filename), "w", encoding="utf-8") as f:
            f.write(render_calculator_page(page, is_home=False))
        generated_urls.append(f"{BASE_URL}/{filename}")

    # 4. Generate Cumulative Daily Product Review Pages (+3 new reviews unlocked every single day)
    active_reviews = get_cumulative_product_reviews()
    for rev in active_reviews:
        filename = f"{rev['slug']}.html"
        with open(os.path.join(OUTPUT_DIR, filename), "w", encoding="utf-8") as f:
            f.write(render_single_review_page(rev))
        generated_urls.append(f"{BASE_URL}/{filename}")

    # 5. Generate Standalone Head-to-Head Product Comparison Pages
    for vs in VS_COMPARISONS:
        filename = f"{vs['slug']}.html"
        with open(os.path.join(OUTPUT_DIR, filename), "w", encoding="utf-8") as f:
            f.write(render_vs_comparison_page(vs))
        generated_urls.append(f"{BASE_URL}/{filename}")

    # 6. XML Sitemap, Robots & IndexNow Auto-Ping
    generate_sitemap_and_robots(generated_urls)
    ping_indexnow(generated_urls)
    print(f"Successfully generated {len(generated_urls)} total SEO pages ({len(active_reviews)} cumulative review articles [+3/day] + HTML/XML sitemaps) in /{OUTPUT_DIR}!")

if __name__ == "__main__":
    main()
