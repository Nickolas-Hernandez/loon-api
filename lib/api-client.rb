require 'net/http'
require 'json'
require 'uri'

class ApiClient
  BASE_URL = "https://moon-phase.p.rapidapi.com"
  API_KEY = ENV['LUNAR_API_TOKEN']

  def self.get(endpoint, params = {})
    url = URI("#{BASE_URL}/#{endpoint}")
    url.query = URI.encode_www_form(params) unless params.empty?

    request = Net::HTTP::Get.new(url)
    request["x-rapidapi-key"] = API_KEY

    response = make_request(url, request)
    parse_response(response)
  end

  private

  def self.make_request(url, request)
    Net::HTTP.start(url.hostname, url.port, use_ssl: true) do |http|
      http.request(request)
    end
  end

  def self.parse_response(response)
    if response.is_a?(Net::HTTPSuccess)
      JSON.parse(response.body)
    else
      { error: "Request failed with status: #{response.code}" }
    end
  end
end