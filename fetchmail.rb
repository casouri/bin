def on_battery
  connection_info = `system_profiler SPPowerDataType`.match(/Connected: (.+?)\n/)[1]
  if connection_info == 'Yes' then
    return false
  else
    return true
  end
end

$interval = 0

def maybe_fetchmail
  while true do
    if on_battery then
      puts 'On battery'
      if $interval >= 10 then # 10 min
        fetchmail
        $interval = 0
      else
        $interval += 1
      end
    else
      puts 'On AC'
      fetchmail
    end
    sleep 60
  end
end

def fetchmail
  puts "Fetching"
  system('mbsync gmail')
  system('mbsync psu')
end

maybe_fetchmail
