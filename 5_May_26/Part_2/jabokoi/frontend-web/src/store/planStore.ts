import { create } from 'zustand';

interface TripPlan {
  id: string;
  destination: string;
  startDate: string;
  endDate: string;
  itinerary: any[];
  totalBudget: number;
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
