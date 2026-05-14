import { create } from 'zustand';

interface TripPlan {
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
}

interface PlanState {
  activePlan: TripPlan | null;
  setActivePlan: (plan: TripPlan) => void;
  clearPlan: () => void;
}

export const usePlanStore = create<PlanState>((set) => ({
  activePlan: null,
  setActivePlan: (plan) => set({ activePlan: plan }),
  clearPlan: () => set({ activePlan: null }),
}));
