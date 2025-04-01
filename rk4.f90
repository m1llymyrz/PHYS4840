program RungeKutta2
    implicit none
    real(8) :: t, x, dt, k1, k2, k3, k4, t_end ! iounit can be set so that I dont have to reset the unit number
    integer :: n, i
    
    ! Define initial conditions
    t = 0.0d0      ! Initial time
    x = 1.0d0      ! Initial condition for x
    dt = 0.1d0     ! Time step
    t_end = 10.0d0 ! Final time
    
    ! Number of time steps
    n = int((t_end - t) / dt) ! switching back to 10000 for in-class question 3
    
    ! Open a file to store results
    open(unit=24, file="rk4_results.dat", status="replace") ! Unit number is arbitrary; might have to make status='new'
    write(24,*) "t x" ! This writes the column header as a string
    write(24,*) t, x
    
    ! RK2 integration loop
    do i = 1, n !Fortran uses "do" loops
        k1 = dt * (-x**3 + sin(t))
        k2 = dt * (-(x + 0.5d0*k1)**3 + sin(t + 0.5d0*dt))
        k3 = dt * (-(x + 0.5d0*k2)**3 + sin(t + 0.5d0*dt))
        k4 = dt * (-(x + k3)**3 + sin(t + dt))

        x = ((1/6)*k1 + (1/6)*2*k2 + (1/6)*2*k3 + (1/6)*k4)
        t = t + dt
        
        ! Write results to file
        write(24,*) t, x
    end do
    
    ! Close file
    close(24) ! Fortran requires a close statement otherwise we will get an error
    
    print *, "Integration complete. Results saved to rk4_results.dat"
    
end program RungeKutta2