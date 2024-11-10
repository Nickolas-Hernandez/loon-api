# daily_moon.rb
class DailyMoon
  attr_accessor :timestamp, :datestamp, :moon_phase, :illumination,
                :day, :age, :rise, :set, :altitude

  def initialize(datestamp:, moon_phase:, illumination:, day:, age:, rise:, set:, altitude:)
    @datestamp = datestamp
    @timestamp = Time.now.to_i
    @moon_phase = moon_phase
    @illumination = illumination
    @day = day
    @age = age
    @rise = rise
    @set = set
    @altitude = altitude
  end

  def to_hash
    {
      timestamp: @timestamp,
      datestamp: @datestamp,
      moon_phase: @moon_phase,
      illumination: @illumination,
      day: @day,
      age: @age,
      rise: @rise,
      set: @set,
      altitude: @altitude
    }
  end
end