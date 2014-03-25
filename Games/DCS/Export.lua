-- create socket and connect to server
function LuaExportStart()
	package.path  = package.path..";.\\LuaSocket\\?.lua"
	package.cpath = package.cpath..";.\\LuaSocket\\?.dll"
	socket = require("socket")
	
	host = host or "10.20.0.90"
	port = port or 50007

	c = socket.try(socket.connect(host, port))
	c:setoption("tcp-nodelay",true)
end

-- close socket
function LuaExportStop()
	c:close()
end

-- unused
function LuaExportBeforeNextFrame()
	-- Function is needed in order to have a proper working export, even if its empty
	--socket.try(c:send("before next event\n"))
end

-- unused
function LuaExportAfterNextFrame()
	-- Function is needed in order to have a proper working export, even if its empty
	--socket.try(c:send("after next event\n"))
end

-- export roll/pitch info through socket
function LuaExportActivityNextEvent(t)
	local pitch,roll,yaw = LoGetADIPitchBankYaw()
	local message = string.format("Roll:%.2f|Pitch:%.2f\n", radToDegree(roll), radToDegree(pitch))
	socket.try(c:send(message))
	-- run every 0.1 seconds
	return t + 0.1
end

-- convert radians to degree
function radToDegree(rad)
	local factor = 57.2957795131
	return rad * factor
end
