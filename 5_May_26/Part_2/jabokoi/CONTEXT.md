# Jabo Koi — Project Context File
> "যাবো কই?" — AI-powered travel planning app for Bangladesh
> Last updated: May 2026

---

## 1. Project overview

**Jabo Koi** (যাবো কই — "Where shall we go?") is a conversational AI travel planning application built specifically for Bangladesh. It serves two user groups: locals looking for domestic travel ideas, and Non-Resident Bangladeshis (NRBs) planning trips back home. The core experience is a chat interface where an AI bot asks users about their budget, hotel preferences, food spending, and travel dates — then generates a personalized, weather-aware trip plan with editable itineraries and booking options in BDT.

**Problem being solved:** There is no AI-native travel planner for Bangladesh. Existing tools (TripAdvisor, Booking.com) show USD pricing, have no monsoon awareness, and offer no conversational guidance. Bangladeshis — both at home and abroad — struggle to plan trips without knowing what is safe, affordable, and currently accessible.

---

## 2. Target users

### User Group A — Local travelers
- Residents of Dhaka, Chittagong, Sylhet planning weekend or holiday trips
- Budget-conscious; need BDT pricing
- Prefer Bengali or English
- Device: mid-range Android (Symphony, Samsung A-series, Walton)

### User Group B — NRB / diaspora
- Bangladeshis living in UK, USA, UAE, Saudi Arabia, Malaysia
- Higher disposable income; comfortable with USD but want BDT context
- Visiting Bangladesh 1–2 times per year
- Device: iPhone or flagship Android

---

## 3. Core features

| Feature | Description |
|---|---|
| Conversational intake | Bot progressively collects: destination preference, travel dates, party size, total budget, hotel budget/night, food budget/day |
| Weather-aware suggestions | Checks current + forecasted weather before recommending destinations; warns about monsoon/flood risks |
| AI trip plan generation | Full day-by-day itinerary with hotel options, restaurants, transport, and activities within budget |
| Editable plan | User can swap hotels, change days, remove activities; bot recalculates budget live |
| Booking integration | Links to Shohoz (bus), Biman/US-Bangla (flights), Agoda/Booking.com (hotels) |
| BDT-native budgeting | All pricing in Bangladeshi Taka; optional USD mode for NRB users |
| Bengali + English | Supports Bangla script input and English; auto-detects language |
| Seasonal intelligence | Built-in knowledge of monsoon seasons, road closures, and destination availability |

---

## 4. Tech stack

### 4.1 Frontend — Web
- **Framework:** React (Vite)
- **Language:** TypeScript
- **Styling:** Tailwind CSS
- **State management:** Zustand
- **Chat UI:** Custom component
- **Maps:** Google Maps JavaScript API
- **HTTP client:** Axios

### 4.2 Frontend — Mobile
- **Framework:** React Native (Expo)
- **Language:** TypeScript
- **Navigation:** React Navigation v6
- **State management:** Zustand (shared logic with web where possible)
- **Maps:** react-native-maps
- **Push notifications:** Expo Notifications
- **Platform priority:** Android-first (97% Android market share in Bangladesh), then iOS
- **Target devices:** Mid-range Android (3GB RAM minimum)

### 4.3 Backend
- **Framework:** Django (Python 3.12+)
- **API layer:** Django REST Framework (DRF)
- **Authentication:** JWT via djangorestframework-simplejwt
- **Auth method:** Email + password
- **Task queue:** Celery + Redis (for async plan generation and weather checks)
- **ORM:** Django ORM with PostgreSQL
- **Admin panel:** Django Admin (for managing destination data, hotels, and content)

### 4.4 Database
- **Primary DB:** PostgreSQL
- **Cache:** Redis (session data, weather API cache, rate limiting)
- **Storage:** AWS S3 or DigitalOcean Spaces (destination images, user uploads)

### 4.5 AI layer
- **Provider:** Anthropic Claude API (`claude-sonnet-4-6`)
- **Usage:** Conversation management, intent extraction, budget parsing, trip plan generation, Bengali language support
- **Pattern:** Each conversation turn sends full message history + system prompt to Claude API; response streamed back to client

### 4.6 Third-party integrations

| Service | Purpose | API |
|---|---|---|
| OpenWeatherMap | Current + forecast weather for BD cities | REST API |
| Shohoz | Bus ticket search and booking | Partner API |
| Biman Bangladesh / US-Bangla | Domestic flight info | Scraping / affiliate |
| Agoda / Booking.com | Hotel listings in BDT | Affiliate API |
| bKash | Mobile payment (local users) | bKash Payment Gateway |
| Nagad | Mobile payment (alternative) | Nagad API |
| Google Maps Platform | Maps, directions, place search | Maps JS + Places API |
| Firebase | Push notifications (mobile) | FCM |

---

## 5. Dataset — what we store

### 5.1 Destinations
```
Destination
├── id (UUID)
├── name_en (string)
├── name_bn (string)
├── division (string)
├── type (enum) — beach / hill / forest / historical / lake / city
├── description_en (text)
├── description_bn (text)
├── best_months (array of int) — [10, 11, 12, 1, 2, 3]
├── avoid_months (array of int) — [6, 7, 8, 9]
├── monsoon_risk (enum) — low / medium / high
├── flood_risk (boolean)
├── road_access_monsoon (boolean)
├── lat (float)
├── lng (float)
├── weather_city_id (string) — OpenWeatherMap city ID
├── images (array of S3 URLs)
├── tags (array) — ["UNESCO", "family", "trekking", "beach"]
├── min_days_recommended (int)
├── max_days_recommended (int)
└── is_active (boolean)
```

### 5.2 Hotels
```
Hotel
├── id (UUID)
├── destination (FK → Destination)
├── name (string)
├── name_bn (string)
├── star_rating (int 1–5)
├── price_per_night_bdt (int)
├── price_tier (enum) — budget / midrange / premium
├── amenities (array) — ["AC", "WiFi", "pool", "restaurant"]
├── booking_url (string)
├── agoda_id (string, nullable)
├── phone (string)
├── address (string)
├── lat (float)
├── lng (float)
└── is_active (boolean)
```

### 5.3 Restaurants
```
Restaurant
├── id (UUID)
├── destination (FK → Destination)
├── name (string)
├── cuisine_type (string)
├── avg_meal_cost_bdt (int)
├── price_tier (enum) — budget / midrange / premium
├── google_place_id (string)
├── lat (float)
├── lng (float)
└── is_active (boolean)
```

### 5.4 Activities
```
Activity
├── id (UUID)
├── destination (FK → Destination)
├── name_en (string)
├── name_bn (string)
├── description_en (text)
├── duration_hours (float)
├── cost_bdt (int) — 0 if free
├── type (enum) — sightseeing / adventure / cultural / nature / food
├── best_time_of_day (enum) — morning / afternoon / evening / any
└── is_monsoon_available (boolean)
```

### 5.5 Transport routes
```
TransportRoute
├── id (UUID)
├── origin_city (string)
├── destination_city (string)
├── mode (enum) — bus / train / launch / flight / CNG / microbus
├── operator (string)
├── avg_duration_minutes (int)
├── avg_cost_bdt (int)
├── booking_url (string, nullable)
├── notes (text)
└── is_active (boolean)
```

### 5.6 Users
```
User
├── id (UUID)
├── email (string) — primary identifier
├── password (hashed)
├── name (string)
├── preferred_language (enum) — bn / en
├── is_nrb (boolean)
├── country_of_residence (string, nullable)
├── currency_preference (enum) — BDT / USD
├── created_at (datetime)
└── last_active (datetime)
```

### 5.7 Conversations & trip plans
```
Conversation
├── id (UUID)
├── user (FK → User)
├── messages (JSONB) — full chat history array
├── status (enum) — active / plan_generated / booked / abandoned
├── created_at (datetime)
└── updated_at (datetime)

TripPlan
├── id (UUID)
├── conversation (FK → Conversation)
├── user (FK → User)
├── destination (FK → Destination)
├── start_date (date)
├── end_date (date)
├── party_size (int)
├── total_budget_bdt (int)
├── hotel_budget_per_night_bdt (int)
├── food_budget_per_day_bdt (int)
├── plan_data (JSONB) — full itinerary JSON
├── is_edited (boolean)
├── created_at (datetime)
└── updated_at (datetime)
```

---

## 6. Django project structure

```
jabokoi/
├── manage.py
├── requirements.txt
├── .env
├── config/
│   ├── settings/
│   │   ├── base.py
│   │   ├── development.py
│   │   └── production.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── apps/
│   ├── users/
│   │   ├── models.py
│   │   ├── serializers.py
│   │   ├── views.py
│   │   └── urls.py
│   ├── destinations/
│   │   ├── models.py
│   │   ├── serializers.py
│   │   ├── views.py
│   │   ├── admin.py
│   │   └── urls.py
│   ├── chat/
│   │   ├── models.py
│   │   ├── serializers.py
│   │   ├── views.py
│   │   ├── claude_service.py
│   │   ├── weather_service.py
│   │   └── urls.py
│   ├── bookings/
│   │   ├── models.py
│   │   ├── views.py
│   │   └── urls.py
│   └── payments/
│       ├── models.py
│       ├── bkash_service.py
│       └── views.py
├── data/
│   └── fixtures/
│       ├── destinations.json
│       ├── hotels.json
│       ├── activities.json
│       └── transport_routes.json
└── scripts/
    └── seed_data.py
```

---

## 7. React web project structure

```
frontend-web/
├── package.json
├── vite.config.ts
├── src/
│   ├── main.tsx
│   ├── App.tsx
│   ├── api/
│   │   ├── auth.ts
│   │   ├── chat.ts
│   │   └── destinations.ts
│   ├── components/
│   │   ├── chat/
│   │   │   ├── ChatWindow.tsx
│   │   │   ├── MessageBubble.tsx
│   │   │   └── TypingIndicator.tsx
│   │   ├── plan/
│   │   │   ├── TripPlanCard.tsx
│   │   │   ├── DayItinerary.tsx
│   │   │   ├── BudgetBreakdown.tsx
│   │   │   └── EditPlanModal.tsx
│   │   ├── booking/
│   │   │   ├── HotelOptions.tsx
│   │   │   ├── TransportOptions.tsx
│   │   │   └── BookingConfirm.tsx
│   │   └── shared/
│   │       ├── WeatherBadge.tsx
│   │       ├── BudgetPill.tsx
│   │       └── LanguageToggle.tsx
│   ├── store/
│   │   ├── authStore.ts
│   │   ├── chatStore.ts
│   │   ├── planStore.ts
│   │   └── userStore.ts
│   ├── pages/
│   │   ├── Login.tsx
│   │   ├── Register.tsx
│   │   ├── Home.tsx
│   │   ├── Chat.tsx
│   │   ├── PlanView.tsx
│   │   └── Profile.tsx
│   └── utils/
│       ├── currency.ts
│       ├── dates.ts
│       └── season.ts
```

---

## 8. React Native mobile project structure

```
frontend-mobile/
├── package.json
├── app.json
├── App.tsx
├── src/
│   ├── navigation/
│   │   ├── RootNavigator.tsx
│   │   ├── AuthNavigator.tsx
│   │   └── MainNavigator.tsx
│   ├── screens/
│   │   ├── LoginScreen.tsx
│   │   ├── RegisterScreen.tsx
│   │   ├── Onboarding.tsx
│   │   ├── Chat.tsx
│   │   ├── PlanView.tsx
│   │   ├── Destinations.tsx
│   │   └── Profile.tsx
│   ├── components/
│   │   ├── chat/
│   │   ├── plan/
│   │   └── shared/
│   ├── store/
│   ├── services/
│   │   ├── api.ts
│   │   ├── notifications.ts
│   │   └── storage.ts
│   └── utils/
│       ├── currency.ts
│       └── season.ts
```

---

## 9. Claude AI system prompt (base)

```
You are the Jabo Koi (যাবো কই) travel assistant — an AI built specifically for Bangladesh travel planning. You speak Bengali and English fluently. Your name means "Where shall we go?" and your job is to help users plan trips within Bangladesh by asking about their budget, dates, and preferences — then generating a detailed, realistic travel plan.

Rules:
- Always check the current month/season before suggesting destinations
- Warn users if their chosen destination is risky during monsoon (June–September)
- All prices must be in BDT (Bangladeshi Taka) unless user requests USD
- Ask one question at a time — do not overwhelm the user
- Budget categories: Budget (under ৳15,000 total), Mid-range (৳15,000–৳40,000), Premium (৳40,000+)
- Hotel budget categories: Budget (under ৳1,500/night), Mid (৳1,500–৳4,000), Premium (৳4,000+)
- When generating a plan, include: transport from Dhaka, hotel recommendation, day-by-day activities, food suggestions, and total estimated cost breakdown
- If user is NRB, acknowledge they may not know current BD prices and be extra clear
- Keep responses concise and friendly. Use "ভাই/আপু" tone when speaking Bengali.
```

---

## 10. Key destinations reference

| Destination | Division | Type | Best months | Monsoon risk |
|---|---|---|---|---|
| Cox's Bazar | Chittagong | Beach | Oct–Mar | Medium |
| Sundarbans | Khulna | Forest/Mangrove | Nov–Feb | High (closes Jun–Sep) |
| Sylhet | Sylhet | Tea/Hills | Oct–Apr | Low |
| Bandarban | Chittagong | Hill tracts | Oct–Mar | High (road flooding) |
| Rangamati | Chittagong | Lake | Oct–Mar | High |
| Sreemangal | Sylhet | Tea garden | Oct–Apr | Low |
| Kuakata | Barisal | Beach | Nov–Feb | High |
| Paharpur | Rajshahi | Historical | Oct–Mar | Low |
| Saint Martin's Island | Chittagong | Island | Nov–Feb | Very high (closes May–Oct) |
| Jaflong | Sylhet | Nature | Oct–Apr | Medium |

---

## 11. Budget tiers (BDT)

| Tier | Total trip | Hotel/night | Food/day | Transport |
|---|---|---|---|---|
| Budget | ৳8,000–15,000 | ৳800–1,500 | ৳300–600 | Bus / launch |
| Mid-range | ৳15,000–40,000 | ৳1,500–4,000 | ৳600–1,200 | AC bus / flight |
| Premium | ৳40,000+ | ৳4,000+ | ৳1,200+ | Domestic flight |

---

## 12. Environment variables (.env)

```env
# Django
SECRET_KEY=
DEBUG=False
ALLOWED_HOSTS=

# Database
DATABASE_URL=postgresql://user:password@localhost:5432/jabokoi

# Redis
REDIS_URL=redis://localhost:6379/0

# Claude API
ANTHROPIC_API_KEY=

# Weather
OPENWEATHER_API_KEY=

# AWS / Storage
AWS_ACCESS_KEY_ID=
AWS_SECRET_ACCESS_KEY=
AWS_STORAGE_BUCKET_NAME=

# bKash
BKASH_APP_KEY=
BKASH_APP_SECRET=
BKASH_USERNAME=
BKASH_PASSWORD=

# Google Maps
GOOGLE_MAPS_API_KEY=

# Firebase
FIREBASE_SERVER_KEY=
```

---

## 13. Decisions log

- [x] App name: **Jabo Koi (যাবো কই)** — confirmed
- [x] Auth method: **Email + password** — confirmed
- [x] Frontend web: **React (Vite + TypeScript + Tailwind)** — confirmed
- [x] Frontend mobile: **React Native (Expo), Android-first** — confirmed
- [x] Backend: **Django + DRF + PostgreSQL** — confirmed
- [x] AI provider: **Anthropic Claude API (`claude-sonnet-4-6`)** — confirmed
- [ ] Shohoz API access — need to contact them for partner API
- [ ] Biman API availability — may need scraping or affiliate redirect
- [ ] Data collection strategy — manual entry vs crawling for hotels/restaurants
- [ ] Launch scope — Dhaka users first or nationwide?
- [ ] Monetization model — affiliate-first or freemium subscription?
