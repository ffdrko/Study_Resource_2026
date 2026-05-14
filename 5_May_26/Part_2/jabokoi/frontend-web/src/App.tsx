import { useEffect, useMemo, useState } from 'react';
import type { FormEvent, ReactNode } from 'react';
import { BrowserRouter as Router, Link, Route, Routes, useNavigate, useParams } from 'react-router-dom';
import './App.css';
import apiClient from './api/apiClient';
import { useAuthStore } from './store/authStore';
import { usePlanStore } from './store/planStore';
import { useChatStore } from './store/chatStore';

type Destination = {
  id: string;
  name_en: string;
  name_bn: string;
  division: string;
  type: string;
  description_en: string;
  monsoon_risk: string;
  best_months: number[];
  hotels: Array<{ id: string; name: string; price_per_night_bdt: number; star_rating: number }>;
  activities: Array<{ id: string; name_en: string; cost_bdt: number; duration_hours: number }>;
};

type TripPlan = {
  id: string;
  destination: string;
  destination_name: string;
  start_date: string;
  end_date: string;
  party_size: number;
  total_budget_bdt: number;
  hotel_budget_per_night_bdt: number;
  food_budget_per_day_bdt: number;
  plan_data: {
    itinerary: Array<{
      day: number;
      activities: Array<{ time: string; activity: string }>;
    }>;
    hotel?: { name: string; price: number; booking_url?: string | null };
    transport?: Array<{
      mode: string;
      operator: string;
      avg_cost_bdt: number;
      avg_duration_minutes: number;
      booking_url?: string | null;
    }>;
    budget_breakdown?: {
      hotel_total: number;
      food_total: number;
      transport_total: number;
    };
  };
};

type ApiUser = {
  id: string;
  email: string;
  username: string;
  preferred_language: string;
  is_nrb: boolean;
  country_of_residence?: string;
  currency_preference?: string;
};

type ChatResponse = {
  message: string;
  conversation?: { id: string; messages: Array<{ role: 'user' | 'assistant'; content: string }> };
  plan?: TripPlan;
  weather?: { condition: string; temp_c: number; description: string; is_risky: boolean };
  needs_more_details?: boolean;
};

const formatCurrency = (value: number) => new Intl.NumberFormat('en-BD').format(value);

function AppShell() {
  const [destinations, setDestinations] = useState<Destination[]>([]);
  const [loadingDestinations, setLoadingDestinations] = useState(true);
  const [destinationError, setDestinationError] = useState<string | null>(null);

  useEffect(() => {
    const loadDestinations = async () => {
      try {
        const response = await apiClient.get<Destination[]>('/destinations/');
        setDestinations(response.data);
      } catch (error) {
        console.error(error);
        setDestinationError('Could not load destinations right now.');
      } finally {
        setLoadingDestinations(false);
      }
    };

    void loadDestinations();
  }, []);

  return (
    <Router>
      <div className="app-shell">
        <header className="topbar">
          <Link to="/" className="brand">
            <span className="brand-mark">যাবো কই</span>
            <span className="brand-subtitle">AI trip planner for Bangladesh</span>
          </Link>
          <nav className="topnav">
            <Link to="/">Explore</Link>
            <Link to="/chat">Planner</Link>
            <Link to="/login">Login</Link>
            <Link to="/register" className="nav-cta">Create account</Link>
          </nav>
        </header>

        <Routes>
          <Route
            path="/"
            element={
              <HomePage
                destinations={destinations}
                loading={loadingDestinations}
                error={destinationError}
              />
            }
          />
          <Route path="/login" element={<LoginPage />} />
          <Route path="/register" element={<RegisterPage />} />
          <Route
            path="/chat"
            element={
              <PlannerPage
                destinations={destinations}
                loading={loadingDestinations}
              />
            }
          />
          <Route
            path="/plan/:id"
            element={<PlanPage destinations={destinations} />}
          />
        </Routes>
      </div>
    </Router>
  );
}

function HomePage({
  destinations,
  loading,
  error,
}: {
  destinations: Destination[];
  loading: boolean;
  error: string | null;
}) {
  return (
    <main className="page">
      <section className="hero">
        <div className="hero-copy">
          <p className="eyebrow">Monsoon-aware planning in BDT</p>
          <h1>Plan a Bangladesh trip with live constraints, local budgets, and an AI copilot.</h1>
          <p className="hero-text">
            Jabo Koi helps locals and NRBs turn a loose idea into a real itinerary with hotels,
            transport hints, seasonal risk notes, and a budget breakdown that actually feels local.
          </p>
          <div className="hero-actions">
            <Link to="/chat" className="button button-primary">Start planning</Link>
            <Link to="/register" className="button button-secondary">Create traveler profile</Link>
          </div>
        </div>
        <div className="hero-panel">
          <div className="stat-card">
            <strong>10+</strong>
            <span>core Bangladesh destinations in scope</span>
          </div>
          <div className="stat-card">
            <strong>BDT first</strong>
            <span>budgeting for transport, food, and stay</span>
          </div>
          <div className="stat-card">
            <strong>Rain-aware</strong>
            <span>season alerts before the plan is generated</span>
          </div>
        </div>
      </section>

      <section className="section">
        <div className="section-heading">
          <h2>Featured destinations</h2>
          <p>Pick a starting point, then fine-tune dates and budget in the planner.</p>
        </div>
        {loading && <div className="empty-state">Loading destinations...</div>}
        {error && <div className="empty-state error">{error}</div>}
        {!loading && !error && (
          <div className="destination-grid">
            {destinations.map((destination) => (
              <article key={destination.id} className="destination-card">
                <div className="destination-header">
                  <div>
                    <h3>{destination.name_en}</h3>
                    <p>{destination.name_bn}</p>
                  </div>
                  <span className={`risk-pill risk-${destination.monsoon_risk}`}>
                    {destination.monsoon_risk.replace('_', ' ')} risk
                  </span>
                </div>
                <p className="destination-description">{destination.description_en}</p>
                <div className="destination-meta">
                  <span>{destination.division}</span>
                  <span>{destination.type}</span>
                  <span>{destination.hotels.length} hotels</span>
                </div>
                <Link to="/chat" className="button button-secondary button-full">Plan this trip</Link>
              </article>
            ))}
          </div>
        )}
      </section>
    </main>
  );
}

function LoginPage() {
  const navigate = useNavigate();
  const { setAuth } = useAuthStore();
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState<string | null>(null);
  const [isSubmitting, setIsSubmitting] = useState(false);

  const onSubmit = async (event: FormEvent<HTMLFormElement>) => {
    event.preventDefault();
    setIsSubmitting(true);
    setError(null);

    try {
      const loginResponse = await apiClient.post('/users/login/', { email, password });
      const profileResponse = await apiClient.get<ApiUser>('/users/profile/', {
        headers: { Authorization: `Bearer ${loginResponse.data.access}` },
      });
      setAuth(profileResponse.data, loginResponse.data.access);
      navigate('/chat');
    } catch (submitError) {
      console.error(submitError);
      setError('Login failed. Check your email and password.');
    } finally {
      setIsSubmitting(false);
    }
  };

  return (
    <AuthLayout
      title="Welcome back"
      subtitle="Sign in with your email to continue planning."
      footer={<Link to="/register">Need an account? Create one</Link>}
    >
      <form className="auth-form" onSubmit={onSubmit}>
        <label>
          Email
          <input value={email} onChange={(event) => setEmail(event.target.value)} type="email" required />
        </label>
        <label>
          Password
          <input value={password} onChange={(event) => setPassword(event.target.value)} type="password" required />
        </label>
        {error && <p className="form-error">{error}</p>}
        <button className="button button-primary" type="submit" disabled={isSubmitting}>
          {isSubmitting ? 'Signing in...' : 'Sign in'}
        </button>
      </form>
    </AuthLayout>
  );
}

function RegisterPage() {
  const navigate = useNavigate();
  const [form, setForm] = useState({
    email: '',
    username: '',
    password: '',
    preferred_language: 'en',
    is_nrb: false,
    country_of_residence: '',
    currency_preference: 'BDT',
  });
  const [error, setError] = useState<string | null>(null);
  const [isSubmitting, setIsSubmitting] = useState(false);

  const onSubmit = async (event: FormEvent<HTMLFormElement>) => {
    event.preventDefault();
    setIsSubmitting(true);
    setError(null);

    try {
      await apiClient.post('/users/register/', form);
      navigate('/login');
    } catch (submitError) {
      console.error(submitError);
      setError('Registration failed. Try a different email or username.');
    } finally {
      setIsSubmitting(false);
    }
  };

  return (
    <AuthLayout
      title="Create your traveler profile"
      subtitle="Tell Jabo Koi a little about you so it can plan in the right language and currency."
      footer={<Link to="/login">Already registered? Sign in</Link>}
    >
      <form className="auth-form" onSubmit={onSubmit}>
        <label>
          Email
          <input
            value={form.email}
            onChange={(event) => setForm((current) => ({ ...current, email: event.target.value }))}
            type="email"
            required
          />
        </label>
        <label>
          Username
          <input
            value={form.username}
            onChange={(event) => setForm((current) => ({ ...current, username: event.target.value }))}
            required
          />
        </label>
        <label>
          Password
          <input
            value={form.password}
            onChange={(event) => setForm((current) => ({ ...current, password: event.target.value }))}
            type="password"
            required
          />
        </label>
        <div className="two-column">
          <label>
            Preferred language
            <select
              value={form.preferred_language}
              onChange={(event) =>
                setForm((current) => ({ ...current, preferred_language: event.target.value }))
              }
            >
              <option value="en">English</option>
              <option value="bn">Bangla</option>
            </select>
          </label>
          <label>
            Currency
            <select
              value={form.currency_preference}
              onChange={(event) =>
                setForm((current) => ({ ...current, currency_preference: event.target.value }))
              }
            >
              <option value="BDT">BDT</option>
              <option value="USD">USD</option>
            </select>
          </label>
        </div>
        <label className="checkbox">
          <input
            checked={form.is_nrb}
            onChange={(event) => setForm((current) => ({ ...current, is_nrb: event.target.checked }))}
            type="checkbox"
          />
          I’m an NRB / diaspora traveler
        </label>
        <label>
          Country of residence
          <input
            value={form.country_of_residence}
            onChange={(event) =>
              setForm((current) => ({ ...current, country_of_residence: event.target.value }))
            }
          />
        </label>
        {error && <p className="form-error">{error}</p>}
        <button className="button button-primary" type="submit" disabled={isSubmitting}>
          {isSubmitting ? 'Creating account...' : 'Create account'}
        </button>
      </form>
    </AuthLayout>
  );
}

function PlannerPage({ destinations, loading }: { destinations: Destination[]; loading: boolean }) {
  const navigate = useNavigate();
  const { token, logout, user } = useAuthStore();
  const { activePlan, setActivePlan } = usePlanStore();
  const { currentConversationId, messages, setConversation, addMessage } = useChatStore();
  const [planner, setPlanner] = useState({
    destination_name: '',
    start_date: '',
    end_date: '',
    party_size: 2,
    total_budget: 20000,
    hotel_budget: 2500,
    food_budget: 900,
    message: 'Please create a trip plan for me.',
  });
  const [weatherSummary, setWeatherSummary] = useState<string | null>(null);
  const [error, setError] = useState<string | null>(null);
  const [isSubmitting, setIsSubmitting] = useState(false);

  const destinationOptions = useMemo(
    () => destinations.map((destination) => destination.name_en),
    [destinations],
  );

  const selectedDestination = destinations.find(
    (destination) => destination.name_en === planner.destination_name,
  );

  const submitPlanRequest = async (event: FormEvent<HTMLFormElement>) => {
    event.preventDefault();
    if (!token) {
      navigate('/login');
      return;
    }

    setIsSubmitting(true);
    setError(null);
    addMessage({ role: 'user', content: planner.message });

    try {
      const response = await apiClient.post<ChatResponse>('/chat/send/', {
        conversation_id: currentConversationId,
        ...planner,
      });

      if (response.data.conversation) {
        setConversation(response.data.conversation.id, response.data.conversation.messages);
      }
      if (response.data.message && !response.data.conversation) {
        addMessage({ role: 'assistant', content: response.data.message });
      }
      if (response.data.plan) {
        setActivePlan(response.data.plan);
        navigate(`/plan/${response.data.plan.id}`);
      }
      if (response.data.weather) {
        setWeatherSummary(
          `${response.data.weather.condition}, ${response.data.weather.temp_c}°C. ${response.data.weather.description}`,
        );
      }
    } catch (submitError) {
      console.error(submitError);
      setError('We could not generate the plan. Please review the trip details and try again.');
    } finally {
      setIsSubmitting(false);
    }
  };

  return (
    <main className="page planner-page">
      <section className="planner-header">
        <div>
          <p className="eyebrow">Interactive planner</p>
          <h1>Build a monsoon-aware Bangladesh itinerary</h1>
          <p>
            {user
              ? `Planning as ${user.email}.`
              : 'Sign in to generate plans, save conversations, and move toward booking.'}
          </p>
        </div>
        {token && (
          <button className="button button-secondary" onClick={logout} type="button">
            Logout
          </button>
        )}
      </section>

      <div className="planner-grid">
        <form className="planner-form panel" onSubmit={submitPlanRequest}>
          <div className="panel-heading">
            <h2>Trip inputs</h2>
            <p>Fill out the essentials and the planner will generate a first draft.</p>
          </div>

          {loading ? (
            <div className="empty-state">Loading destination list...</div>
          ) : (
            <>
              <label>
                Destination
                <select
                  value={planner.destination_name}
                  onChange={(event) =>
                    setPlanner((current) => ({ ...current, destination_name: event.target.value }))
                  }
                  required
                >
                  <option value="">Choose a destination</option>
                  {destinationOptions.map((option) => (
                    <option key={option} value={option}>
                      {option}
                    </option>
                  ))}
                </select>
              </label>

              <div className="two-column">
                <label>
                  Start date
                  <input
                    type="date"
                    value={planner.start_date}
                    onChange={(event) =>
                      setPlanner((current) => ({ ...current, start_date: event.target.value }))
                    }
                    required
                  />
                </label>
                <label>
                  End date
                  <input
                    type="date"
                    value={planner.end_date}
                    onChange={(event) =>
                      setPlanner((current) => ({ ...current, end_date: event.target.value }))
                    }
                    required
                  />
                </label>
              </div>

              <div className="two-column">
                <label>
                  Party size
                  <input
                    type="number"
                    min={1}
                    value={planner.party_size}
                    onChange={(event) =>
                      setPlanner((current) => ({ ...current, party_size: Number(event.target.value) }))
                    }
                    required
                  />
                </label>
                <label>
                  Total budget (BDT)
                  <input
                    type="number"
                    min={0}
                    value={planner.total_budget}
                    onChange={(event) =>
                      setPlanner((current) => ({ ...current, total_budget: Number(event.target.value) }))
                    }
                    required
                  />
                </label>
              </div>

              <div className="two-column">
                <label>
                  Hotel budget / night
                  <input
                    type="number"
                    min={0}
                    value={planner.hotel_budget}
                    onChange={(event) =>
                      setPlanner((current) => ({ ...current, hotel_budget: Number(event.target.value) }))
                    }
                    required
                  />
                </label>
                <label>
                  Food budget / day
                  <input
                    type="number"
                    min={0}
                    value={planner.food_budget}
                    onChange={(event) =>
                      setPlanner((current) => ({ ...current, food_budget: Number(event.target.value) }))
                    }
                    required
                  />
                </label>
              </div>

              <label>
                Extra note for the planner
                <textarea
                  rows={4}
                  value={planner.message}
                  onChange={(event) =>
                    setPlanner((current) => ({ ...current, message: event.target.value }))
                  }
                />
              </label>
            </>
          )}

          {weatherSummary && <div className="info-banner">{weatherSummary}</div>}
          {error && <div className="empty-state error">{error}</div>}

          <button className="button button-primary" type="submit" disabled={isSubmitting || loading}>
            {isSubmitting ? 'Generating plan...' : 'Generate trip plan'}
          </button>
        </form>

        <aside className="planner-sidebar">
          <section className="panel">
            <div className="panel-heading">
              <h2>Conversation</h2>
              <p>Assistant updates and planning history appear here.</p>
            </div>
            <div className="chat-stack">
              {messages.length === 0 && (
                <div className="empty-state">Your planning conversation will appear here.</div>
              )}
              {messages.map((message, index) => (
                <div key={`${message.role}-${index}`} className={`chat-bubble chat-${message.role}`}>
                  <span>{message.role === 'assistant' ? 'Jabo Koi' : 'You'}</span>
                  <p>{message.content}</p>
                </div>
              ))}
            </div>
          </section>

          <section className="panel">
            <div className="panel-heading">
              <h2>Destination snapshot</h2>
              <p>A quick sense-check before you generate the itinerary.</p>
            </div>
            {selectedDestination ? (
              <div className="snapshot">
                <h3>{selectedDestination.name_en}</h3>
                <p>{selectedDestination.description_en}</p>
                <div className="snapshot-list">
                  <span>{selectedDestination.division}</span>
                  <span>{selectedDestination.type}</span>
                  <span>{selectedDestination.hotels.length} stays</span>
                  <span>{selectedDestination.activities.length} activities</span>
                </div>
              </div>
            ) : (
              <div className="empty-state">Select a destination to preview the travel context.</div>
            )}
            {activePlan && (
              <Link className="button button-secondary button-full" to={`/plan/${activePlan.id}`}>
                Open active plan
              </Link>
            )}
          </section>
        </aside>
      </div>
    </main>
  );
}

function PlanPage({ destinations }: { destinations: Destination[] }) {
  const { id } = useParams();
  const { activePlan } = usePlanStore();
  const [plan, setPlan] = useState<TripPlan | null>(activePlan as TripPlan | null);
  const [bookingMessage, setBookingMessage] = useState<string | null>(null);

  useEffect(() => {
    const loadPlan = async () => {
      if (activePlan && activePlan.id === id) {
        return;
      }

      try {
        const response = await apiClient.get<TripPlan>(`/chat/plans/${id}/`);
        setPlan(response.data);
      } catch (error) {
        console.error(error);
      }
    };

    if (id) {
      void loadPlan();
    }
  }, [activePlan, id]);

  const destination = destinations.find((item) => item.id === plan?.destination);

  const createMockBooking = async (bookingType: 'hotel' | 'transport') => {
    if (!plan) {
      return;
    }

    try {
      const response = await apiClient.post('/bookings/', {
        trip_plan: plan.id,
        booking_type: bookingType,
        amount_bdt:
          bookingType === 'hotel'
            ? plan.plan_data.hotel?.price ?? plan.hotel_budget_per_night_bdt
            : plan.plan_data.budget_breakdown?.transport_total ?? 0,
      });
      await apiClient.post('/payments/', {
        booking: response.data.id,
        amount: response.data.amount_bdt,
        method: 'bkash',
      });
      setBookingMessage(`Mock ${bookingType} booking completed and paid.`);
    } catch (error) {
      console.error(error);
      setBookingMessage('Booking simulation failed. Make sure you are logged in.');
    }
  };

  if (!plan) {
    return (
      <main className="page">
        <div className="empty-state">No plan loaded yet. Generate one from the planner.</div>
      </main>
    );
  }

  return (
    <main className="page">
      <section className="plan-hero">
        <div>
          <p className="eyebrow">Trip plan ready</p>
          <h1>{plan.destination_name}</h1>
          <p>
            {plan.start_date} to {plan.end_date} for {plan.party_size} travelers with a total budget of ৳
            {formatCurrency(plan.total_budget_bdt)}.
          </p>
        </div>
        <div className="hero-actions">
          <button className="button button-primary" onClick={() => void createMockBooking('hotel')} type="button">
            Mock hotel booking
          </button>
          <button className="button button-secondary" onClick={() => void createMockBooking('transport')} type="button">
            Mock transport booking
          </button>
        </div>
      </section>

      {bookingMessage && <div className="info-banner">{bookingMessage}</div>}

      <div className="plan-grid">
        <section className="panel">
          <div className="panel-heading">
            <h2>Stay and spend</h2>
            <p>Budget and lodging details generated from your trip inputs.</p>
          </div>
          <div className="budget-grid">
            <div className="budget-card">
              <span>Hotel</span>
              <strong>{plan.plan_data.hotel?.name ?? 'Standard Hotel'}</strong>
              <p>৳{formatCurrency(plan.plan_data.hotel?.price ?? plan.hotel_budget_per_night_bdt)} per night</p>
            </div>
            <div className="budget-card">
              <span>Food</span>
              <strong>৳{formatCurrency(plan.food_budget_per_day_bdt)}</strong>
              <p>Estimated daily food spend</p>
            </div>
            <div className="budget-card">
              <span>Transport</span>
              <strong>
                ৳{formatCurrency(plan.plan_data.budget_breakdown?.transport_total ?? 0)}
              </strong>
              <p>Suggested route allocation</p>
            </div>
          </div>
          {destination && (
            <div className="destination-notes">
              <h3>Destination note</h3>
              <p>{destination.description_en}</p>
            </div>
          )}
        </section>

        <section className="panel">
          <div className="panel-heading">
            <h2>Day-by-day itinerary</h2>
            <p>A first draft you can refine in later iterations.</p>
          </div>
          <div className="itinerary-list">
            {plan.plan_data.itinerary.map((day) => (
              <article key={day.day} className="itinerary-card">
                <h3>Day {day.day}</h3>
                {day.activities.map((activity, index) => (
                  <div key={`${day.day}-${index}`} className="activity-row">
                    <span>{activity.time}</span>
                    <p>{activity.activity}</p>
                  </div>
                ))}
              </article>
            ))}
          </div>
        </section>
      </div>

      <section className="panel">
        <div className="panel-heading">
          <h2>Transport options</h2>
          <p>Mock route suggestions connected to this destination.</p>
        </div>
        <div className="transport-grid">
          {(plan.plan_data.transport ?? []).length === 0 && (
            <div className="empty-state">No route data yet. Seed transport routes to enrich this section.</div>
          )}
          {(plan.plan_data.transport ?? []).map((route, index) => (
            <article key={`${route.mode}-${index}`} className="transport-card">
              <h3>{route.mode.toUpperCase()}</h3>
              <p>{route.operator}</p>
              <span>৳{formatCurrency(route.avg_cost_bdt)}</span>
              <small>{route.avg_duration_minutes} minutes average</small>
            </article>
          ))}
        </div>
      </section>
    </main>
  );
}

function AuthLayout({
  title,
  subtitle,
  footer,
  children,
}: {
  title: string;
  subtitle: string;
  footer: ReactNode;
  children: ReactNode;
}) {
  return (
    <main className="auth-page">
      <section className="auth-panel">
        <div className="panel-heading">
          <p className="eyebrow">Traveler account</p>
          <h1>{title}</h1>
          <p>{subtitle}</p>
        </div>
        {children}
        <div className="auth-footer">{footer}</div>
      </section>
    </main>
  );
}

function App() {
  return <AppShell />;
}

export default App;
