require 'sinatra'
require 'dotenv/load'
require 'net/http'
require 'uri'
require 'json'
require_relative './lib/api-client'

set :port, 8080

get '/' do
    'Pong'
end

get '/moon-phase' do
  # basic
  # date = params['date']
  # halt 400, { error: "Date parameter is required" }.to_json unless date

  # Use the ApiClient to make a request
  response = ApiClient.get("basic")

  content_type :json
  response.to_json
end

# get '/daily-moon' do 

# end