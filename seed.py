import requests

BASE_URL = "http://localhost:8000"

# products = [
#     # ── Warm / Winter Clothing ──────────────────────────────────────────────
#     {
#         "id": "prod_001",
#         "text": "Heavy wool overcoat for men, double-breasted, ideal for freezing winters and cold commutes"
#     },
#     {
#         "id": "prod_002",
#         "text": "Women's fleece-lined thermal leggings, keeps legs warm in sub-zero temperatures"
#     },
#     {
#         "id": "prod_003",
#         "text": "Unisex down puffer jacket with hood, extremely warm and lightweight, great for snow and hiking"
#     },
#     {
#         "id": "prod_004",
#         "text": "Cashmere turtleneck sweater for women, ultra-soft, perfect for chilly evenings"
#     },
#     {
#         "id": "prod_005",
#         "text": "Men's thermal base layer set, long-sleeve shirt and pants, traps body heat during outdoor activities"
#     },
#     {
#         "id": "prod_006",
#         "text": "Knitted wool beanie hat, unisex, keeps your head and ears warm in cold weather"
#     },
#     {
#         "id": "prod_007",
#         "text": "Sherpa-lined hoodie for men, incredibly cozy for winter lounging or outdoor use"
#     },
#     {
#         "id": "prod_008",
#         "text": "Kids' insulated snow suit, waterproof and warm, designed for playing in the snow"
#     },

#     # ── Summer / Lightweight Clothing ───────────────────────────────────────
#     {
#         "id": "prod_009",
#         "text": "Men's linen short-sleeve shirt, breathable and light, perfect for hot summer days and beach trips"
#     },
#     {
#         "id": "prod_010",
#         "text": "Women's floral sundress, sleeveless, lightweight cotton, ideal for warm weather and outdoor events"
#     },
#     {
#         "id": "prod_011",
#         "text": "Unisex UV-protection rash guard, quick-dry fabric, suitable for swimming and water sports"
#     },
#     {
#         "id": "prod_012",
#         "text": "Men's cargo shorts, moisture-wicking, great for hiking in hot climates or casual summer outings"
#     },

#     # ── Footwear ────────────────────────────────────────────────────────────
#     {
#         "id": "prod_013",
#         "text": "Insulated waterproof snow boots for women, non-slip sole, rated for temperatures down to -30°C"
#     },
#     {
#         "id": "prod_014",
#         "text": "Men's trail running shoes, breathable mesh upper, excellent grip for outdoor terrain"
#     },
#     {
#         "id": "prod_015",
#         "text": "Kids' rubber rain boots, colorful designs, keeps feet dry in puddles and rainy weather"
#     },
#     {
#         "id": "prod_016",
#         "text": "Women's open-toe sandals, lightweight and comfortable for summer walking and travel"
#     },

#     # ── Accessories ─────────────────────────────────────────────────────────
#     {
#         "id": "prod_017",
#         "text": "Merino wool scarf, extra long and wide, excellent for wrapping around neck in cold and windy weather"
#     },
#     {
#         "id": "prod_018",
#         "text": "Insulated ski gloves for men, waterproof outer shell, touchscreen-compatible fingertips"
#     },
#     {
#         "id": "prod_019",
#         "text": "Polarized sunglasses, UV400 protection, lightweight frame, ideal for sunny days and driving"
#     },
#     {
#         "id": "prod_020",
#         "text": "Foldable wide-brim sun hat, UPF 50+, protects face and neck from strong summer sun"
#     },

#     # ── Sports & Activewear ─────────────────────────────────────────────────
#     {
#         "id": "prod_021",
#         "text": "Women's yoga pants, high-waist, four-way stretch fabric, suitable for gym, pilates, and casual wear"
#     },
#     {
#         "id": "prod_022",
#         "text": "Men's compression running tights, moisture-wicking, reduces muscle fatigue during long runs"
#     },
#     {
#         "id": "prod_023",
#         "text": "Windproof cycling jacket, lightweight, packable, great for biking in cool and breezy conditions"
#     },
#     {
#         "id": "prod_024",
#         "text": "Heated electric vest for extreme cold, battery-powered, adjustable heat settings for outdoor workers"
#     },

#     # ── Formal / Office ─────────────────────────────────────────────────────
#     {
#         "id": "prod_025",
#         "text": "Men's slim-fit wool suit, classic charcoal grey, suitable for office meetings and formal events"
#     },
#     {
#         "id": "prod_026",
#         "text": "Women's tailored blazer, structured fit, versatile for professional settings or smart casual looks"
#     },
# ]

# more_products = [
#     # ── Rainy / Monsoon Wear ────────────────────────────────────────────────
#     {
#         "id": "prod_027",
#         "text": "Lightweight waterproof rain jacket for men, breathable shell, ideal for monsoon travel and trekking"
#     },
#     {
#         "id": "prod_028",
#         "text": "Women's waterproof trench coat with hood, stylish and practical for rainy city commutes"
#     },
#     {
#         "id": "prod_029",
#         "text": "Quick-dry athletic t-shirt for women, moisture-wicking fabric, perfect for humid summer workouts"
#     },
#     {
#         "id": "prod_030",
#         "text": "Unisex compact travel umbrella, wind-resistant frame, easy to carry during sudden rain showers"
#     },

#     # ── Outdoor & Hiking Gear ───────────────────────────────────────────────
#     {
#         "id": "prod_031",
#         "text": "Men's insulated hiking pants, water-resistant and durable, suitable for mountain trekking in cold weather"
#     },
#     {
#         "id": "prod_032",
#         "text": "Women's lightweight hiking jacket, breathable and windproof, ideal for outdoor adventures"
#     },
#     {
#         "id": "prod_033",
#         "text": "Thermal hiking socks made from merino wool, keeps feet warm and dry during long winter hikes"
#     },
#     {
#         "id": "prod_034",
#         "text": "Convertible cargo hiking pants, zip-off legs transform into shorts for changing weather conditions"
#     },

#     # ── Casual Everyday Clothing ────────────────────────────────────────────
#     {
#         "id": "prod_035",
#         "text": "Oversized cotton hoodie for women, soft fleece interior, comfortable for casual daily wear"
#     },
#     {
#         "id": "prod_036",
#         "text": "Men's relaxed-fit jogger pants, breathable fabric, perfect for lounging or running errands"
#     },
#     {
#         "id": "prod_037",
#         "text": "Classic denim jacket for men, medium wash, versatile layer for cool evenings"
#     },
#     {
#         "id": "prod_038",
#         "text": "Women's oversized flannel shirt, warm brushed cotton, great for layering during autumn"
#     },

#     # ── Sleepwear & Loungewear ──────────────────────────────────────────────
#     {
#         "id": "prod_039",
#         "text": "Men's fleece pajama set, ultra-soft and warm, ideal for cold winter nights"
#     },
#     {
#         "id": "prod_040",
#         "text": "Women's satin sleepwear set, lightweight and breathable for comfortable summer sleeping"
#     },
#     {
#         "id": "prod_041",
#         "text": "Kids' cotton pajamas with cartoon prints, soft fabric suitable for all-night comfort"
#     },

#     # ── Baby & Kids Clothing ────────────────────────────────────────────────
#     {
#         "id": "prod_042",
#         "text": "Baby winter romper with hood and mittens, thick insulated fabric keeps infants warm outdoors"
#     },
#     {
#         "id": "prod_043",
#         "text": "Kids' lightweight summer t-shirt and shorts set, breathable cotton for active play in hot weather"
#     },
#     {
#         "id": "prod_044",
#         "text": "Children's waterproof raincoat with reflective strips, safe and comfortable for rainy school days"
#     },

#     # ── Luxury / Premium Fashion ────────────────────────────────────────────
#     {
#         "id": "prod_045",
#         "text": "Premium leather gloves for men, cashmere lining, elegant winter accessory for formal occasions"
#     },
#     {
#         "id": "prod_046",
#         "text": "Women's silk blouse with long sleeves, elegant and breathable for office or dinner events"
#     },
#     {
#         "id": "prod_047",
#         "text": "Luxury alpaca wool cardigan, extremely soft and warm, handcrafted for premium winter comfort"
#     },

#     # ── Fitness & Training ──────────────────────────────────────────────────
#     {
#         "id": "prod_048",
#         "text": "Men's sleeveless gym tank top, breathable stretch fabric, designed for weightlifting and workouts"
#     },
#     {
#         "id": "prod_049",
#         "text": "Women's seamless sports bra with high support, ideal for running, gym training, and yoga"
#     },
#     {
#         "id": "prod_050",
#         "text": "Compression calf sleeves for athletes, improves circulation and reduces muscle fatigue during sports"
#     },
# ]

# products.extend(more_products)

products = [
    # ── Electronics ──────────────────────────────────────────────────────────
    {
        "id": "prod_051",
        "text": "Wireless noise-cancelling headphones with deep bass and 30-hour battery life for travel and gaming"
    },
    {
        "id": "prod_052",
        "text": "Portable Bluetooth speaker with waterproof design and powerful stereo sound for outdoor parties"
    },
    {
        "id": "prod_053",
        "text": "Smart fitness watch with heart-rate monitor, sleep tracking, and GPS for active lifestyles"
    },
    {
        "id": "prod_054",
        "text": "Mechanical gaming keyboard with RGB backlighting and tactile switches for competitive gaming"
    },
    {
        "id": "prod_055",
        "text": "4K ultra HD smart television with voice assistant support and streaming apps included"
    },

    # ── Mobile Accessories ──────────────────────────────────────────────────
    {
        "id": "prod_056",
        "text": "Fast-charging USB-C power bank with 20000mAh capacity for smartphones and tablets"
    },
    {
        "id": "prod_057",
        "text": "Shockproof phone case with raised edges and camera protection for modern smartphones"
    },
    {
        "id": "prod_058",
        "text": "Wireless charging pad compatible with Android and iPhone devices for convenient desk charging"
    },
    {
        "id": "prod_059",
        "text": "Foldable laptop stand with adjustable height for ergonomic office and study setups"
    },
    {
        "id": "prod_060",
        "text": "Compact wireless mouse with silent clicks and rechargeable battery for office productivity"
    },

    # ── Home & Kitchen ──────────────────────────────────────────────────────
    {
        "id": "prod_061",
        "text": "Non-stick cookware set with durable aluminum construction for everyday cooking and frying"
    },
    {
        "id": "prod_062",
        "text": "Electric rice cooker with automatic keep-warm function and large family-size capacity"
    },
    {
        "id": "prod_063",
        "text": "High-speed blender for smoothies, protein shakes, and frozen fruit drinks"
    },
    {
        "id": "prod_064",
        "text": "Memory foam pillow with cooling gel layer for comfortable neck support during sleep"
    },
    {
        "id": "prod_065",
        "text": "Air fryer with digital touch controls for healthier low-oil cooking and crispy snacks"
    },

    # ── Furniture ───────────────────────────────────────────────────────────
    {
        "id": "prod_066",
        "text": "Ergonomic office chair with lumbar support and adjustable armrests for long working hours"
    },
    {
        "id": "prod_067",
        "text": "Minimalist wooden study desk with storage shelves for home office and students"
    },
    {
        "id": "prod_068",
        "text": "Modern sectional sofa with soft fabric upholstery and deep comfortable seating"
    },
    {
        "id": "prod_069",
        "text": "Queen-size bed frame with under-bed storage and sturdy metal construction"
    },
    {
        "id": "prod_070",
        "text": "Compact bedside table with drawer and charging station for modern bedrooms"
    },

    # ── Beauty & Personal Care ──────────────────────────────────────────────
    {
        "id": "prod_071",
        "text": "Vitamin C facial serum for glowing skin and reducing dark spots and uneven tone"
    },
    {
        "id": "prod_072",
        "text": "Hydrating aloe vera moisturizer suitable for dry and sensitive skin types"
    },
    {
        "id": "prod_073",
        "text": "Professional hair dryer with ionic technology for fast drying and reduced frizz"
    },
    {
        "id": "prod_074",
        "text": "Electric beard trimmer with adjustable precision settings for grooming and styling"
    },
    {
        "id": "prod_075",
        "text": "Organic shampoo and conditioner set for strengthening damaged hair naturally"
    },

    # ── Grocery & Food ──────────────────────────────────────────────────────
    {
        "id": "prod_076",
        "text": "Premium roasted coffee beans with rich aroma and smooth flavor for espresso lovers"
    },
    {
        "id": "prod_077",
        "text": "Organic green tea bags packed with antioxidants for healthy daily refreshment"
    },
    {
        "id": "prod_078",
        "text": "Crunchy peanut butter with high protein content and no artificial preservatives"
    },
    {
        "id": "prod_079",
        "text": "Dark chocolate gift box with assorted premium cocoa flavors for celebrations"
    },
    {
        "id": "prod_080",
        "text": "Healthy mixed nuts snack pack with almonds, cashews, and walnuts for energy boosts"
    },

    # ── Pet Supplies ────────────────────────────────────────────────────────
    {
        "id": "prod_081",
        "text": "Soft orthopedic dog bed with washable cover for large and medium-sized pets"
    },
    {
        "id": "prod_082",
        "text": "Automatic pet water fountain with filtration system for cats and dogs"
    },
    {
        "id": "prod_083",
        "text": "Interactive cat toy with motion sensor and LED lights for indoor entertainment"
    },
    {
        "id": "prod_084",
        "text": "Adjustable pet harness with reflective straps for safe nighttime walking"
    },
    {
        "id": "prod_085",
        "text": "Premium grain-free dog food with chicken and vegetables for healthy digestion"
    },

    # ── Travel & Bags ───────────────────────────────────────────────────────
    {
        "id": "prod_086",
        "text": "Large hard-shell suitcase with spinner wheels and TSA lock for international travel"
    },
    {
        "id": "prod_087",
        "text": "Water-resistant hiking backpack with multiple compartments for camping and trekking"
    },
    {
        "id": "prod_088",
        "text": "Compact travel toiletry organizer with waterproof lining and hanging hook"
    },
    {
        "id": "prod_089",
        "text": "Leather messenger bag for laptops and office essentials with vintage design"
    },
    {
        "id": "prod_090",
        "text": "Anti-theft crossbody travel bag with hidden zippers and RFID protection"
    },

    # ── Toys & Kids ─────────────────────────────────────────────────────────
    {
        "id": "prod_091",
        "text": "Remote control racing car with rechargeable battery and high-speed performance for kids"
    },
    {
        "id": "prod_092",
        "text": "Educational building blocks set that improves creativity and problem-solving skills"
    },
    {
        "id": "prod_093",
        "text": "Soft plush teddy bear with ultra-soft fabric for children and gift occasions"
    },
    {
        "id": "prod_094",
        "text": "Kids art and craft kit with paints, markers, and drawing supplies for creative learning"
    },
    {
        "id": "prod_095",
        "text": "Battery-powered dinosaur toy with realistic sounds and walking motion for children"
    },

    # ── Automotive ──────────────────────────────────────────────────────────
    {
        "id": "prod_096",
        "text": "Portable car vacuum cleaner with strong suction for interior cleaning and maintenance"
    },
    {
        "id": "prod_097",
        "text": "Dash camera with night vision and loop recording for safe driving documentation"
    },
    {
        "id": "prod_098",
        "text": "Car phone mount with 360-degree rotation for hands-free GPS navigation"
    },
    {
        "id": "prod_099",
        "text": "Waterproof motorcycle riding gloves with anti-slip grip and protective padding"
    },
    {
        "id": "prod_100",
        "text": "Heavy-duty jumper cables for emergency vehicle battery charging and roadside assistance"
    },
]

def seed():
    print(f"Seeding {len(products)} products into the vector DB...\n")
    success, failed = 0, 0

    for product in products:
        response = requests.post(f"{BASE_URL}/add-document", json=product)
        if response.status_code == 200:
            print(f"  ✓  {product['id']}  —  {product['text'][:60]}...")
            success += 1
        else:
            print(f"  ✗  {product['id']}  —  ERROR: {response.text}")
            failed += 1

    print(f"\nDone! {success} inserted, {failed} failed.")

    # ── Demo semantic searches ───────────────────────────────────────────────
    demo_queries = [
        ("warm clothes for winter", 3),
        ("something to wear on a hot beach day", 3),
        ("gifts for cold weather", 3),
        ("protect feet from snow", 2),
        ("workout outfit for women", 2),
    ]

    print("\n" + "═" * 60)
    print("DEMO SEMANTIC SEARCHES")
    print("═" * 60)

    for query, n in demo_queries:
        print(f'\nQuery: "{query}"  (top {n} results)')
        resp = requests.post(
            f"{BASE_URL}/search",
            json={"query": query, "num_results": n}
        )
        if resp.status_code == 200:
            data = resp.json()
            for doc_id, doc in zip(data["matched_ids"], data["matched_documents"]):
                print(f"  → [{doc_id}] {doc[:80]}...")
        else:
            print(f"  Search error: {resp.text}")


if __name__ == "__main__":
    seed()